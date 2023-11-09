# Automatic ini Setter
This script will simply run commands to set the ini settings for Ark: Survival Ascended.
This is useful as the game needs additional, non-menu, settings changed to run smoothly on older hardware.

## Installation

This script was made for [python 3.11](https://www.python.org/downloads/release/python-3116/) and should be installed to the path.<br>

Open up a command prompt in the folder where the script is located.<br>
To install the required packages, run the following command in the command prompt:
```bash
pip install -r requirements.txt
```

## Configuration
You can add or remove commands from the `commands.txt` file to suit your needs.
Each command should be on a new line.

### Additional Settings
Global Illumination Quality must be set to high or epic to show drop beams. <br>
The following are optional settings which I personally don't like.

`r.MipMapLODBias 15` - Potato Mode <br>
`r.Water.SingleLayer 0` - No Water <br>
`r.Lumen.DiffuseIndirect.Allow 0` - No Drop Beams <br>
`wp.Runtime.HLOD 0` - Renders fewer trees and rocks, can cause lag spikes

## Usage
1. Log into the game so that you are spawned into a map.
2. Run the script.

The script will run each command in the `commands.txt` file and display a message stating it has finished.

## License
This repository is licensed under the [MIT License](LICENSE).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.