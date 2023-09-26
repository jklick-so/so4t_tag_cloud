# Stack Overflow for Teams Tag Cloud (so4t_tag_cloud)
A Python script that turns the CSV output from the [Stack Overflow for Teams Tag Report](https://github.com/jklick-so/so4t_tag_report) into a a tag cloud, weighting the tags based on how many page views each has. You can see an example of what the output looks like in the Examples directory ([here](https://github.com/jklick-so/so4t_tag_cloud/blob/main/Examples/so4t_tag_cloud_100_tags.png)).

## Requirements
* Python 3.8 or higher ([download](https://www.python.org/downloads/))
* Operating system: Linux, MacOS, or Windows

## Setup

[Download](https://github.com/jklick-so/so4t_tag_cloud/archive/refs/heads/main.zip) and unpack the contents of this repository

**Installing Dependencies**

* Open a terminal window (or, for Windows, a command prompt)
* Navigate to the directory where you unpacked the files
* Install the dependencies: `pip3 install -r requirements.txt`

## Usage
* In a terminal window, navigate to the directory where you unpacked the script. 
* Put the CSV file that was created from the Stack Overflow for Teams Tag Report in the same directory.
* Run the script with the following command: `python3 so4t_tag_cloud.py --csv <filename.csv> --max-tags <number of tags to include>`

> Note: you can omit the `--max-tags` parameter and it will default to 100 tags.

When the script is finished running, it will indicate the image has been exported, along with the name of file. You can see an example of what the output looks like [here](https://github.com/jklick-so/so4t_tag_cloud/blob/main/Examples/so4t_tag_cloud_100_tags.png).

## Support, security, and legal

While the creator of this Python script works at Stack Overflow, it is a labor of love that comes with no formal support from Stack Overflow. 

If you run into issues using the script, please [open an issue](https://github.com/jklick-so/so4t_tag_cloud/issues). You are also welcome to edit the script to suit your needs, steal the code, or do whatever you want with it. It is provided as-is, with no warranty or guarantee of any kind. If the maintainer wasn't so lazy, there would likely be an MIT license file included.

All data is handled locally on the device from which the script is run. The script does not transmit data to other parties, such as Stack Overflow.