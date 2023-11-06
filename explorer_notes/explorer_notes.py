import json
import time

import pyautogui
import re

import requests

with open('button_coords.json', 'r') as f:
    button_coords = json.load(f)


def load_island_notes() -> tuple[list, list]:
    # with open('asa-island-pois.json', 'r') as f:
    #     pois = json.load(f)
    pois = requests.get(
        'https://ark.wiki.gg/api.php?action=queryDataMap&format=json&pageid=72797&revid=520044&continue=0')
    pois = pois.json()
    notes = pois.get('query', {}).get('markers', {}).get('explorer-note', [])
    dossiers = pois.get('query', {}).get('markers', {}).get('dossier', [])
    return notes, dossiers


def click_create_waypoint():
    create_waypoint_x = button_coords['create_waypoint']['x']
    create_waypoint_y = button_coords['create_waypoint']['y']
    pyautogui.moveTo(create_waypoint_x, create_waypoint_y)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.2)


def click_name():
    name_x = button_coords['name']['x']
    name_y = button_coords['name']['y']
    pyautogui.moveTo(name_x, name_y)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    for x in range(12):
        pyautogui.press('delete')


def click_lat():
    lat_x = button_coords['lat']['x']
    lat_y = button_coords['lat']['y']
    pyautogui.moveTo(lat_x, lat_y)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    for x in range(6):
        pyautogui.press('delete')


def click_lon():
    lon_x = button_coords['lon']['x']
    lon_y = button_coords['lon']['y']
    pyautogui.moveTo(lon_x, lon_y)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    for x in range(6):
        pyautogui.press('delete')


def click_accept():
    accept_x = button_coords['accept']['x']
    accept_y = button_coords['accept']['y']
    pyautogui.moveTo(accept_x, accept_y)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.2)


def create_waypoint(x: int, y: int, name: str):
    click_create_waypoint()
    # fill out the name
    click_name()
    pyautogui.typewrite(name)
    time.sleep(0.1)
    # fill out the latitude
    click_lat()
    pyautogui.typewrite(str(x))
    time.sleep(0.1)
    # fill out the longitude
    click_lon()
    pyautogui.typewrite(str(y))
    time.sleep(0.1)
    # click accept
    click_accept()


def create_waypoints(waypoints: list, order: list[int]) -> None:
    for waypoint in waypoints:
        x = waypoint[1]
        y = waypoint[0]
        name = waypoint[2]
        found = False
        for i in order:
            if f'(ID: {i})' in name:
                found = True
                break
        if not found:
            continue
        # Remove the html span tag garbage
        name = re.sub(r' <span.*?>', '', name)
        create_waypoint(x, y, name)


def main():
    # Assume map is island
    notes, dossiers = load_island_notes()
    waypoints = notes + dossiers
    with open('order.json', 'r') as f:
        order = json.load(f)
    print("Loading notes completed successfully, will start creating waypoints in 10 seconds.\n"
          "Please ensure the game is in windowed mode and the map is open, ready to create waypoints."
          "Please ensure that no other waypoints are on the map.")
    time.sleep(10)
    # Split the waypoints into batches of 16
    waypoints = [waypoints[x:x + 16] for x in range(0, len(waypoints), 16)]
    for waypoints_batch in waypoints:
        create_waypoints(waypoints_batch, order)
        pyautogui.alert("Finished creating waypoints for this batch, Click OK to create waypoints for the next batch.")
        time.sleep(1)
    pyautogui.alert("Finished creating waypoints for all batches, Click OK to exit.")


if __name__ == '__main__':
    main()
