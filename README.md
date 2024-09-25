## A Logger for the CPU Temperature of My Raspberry Pi 5

This repository is used to log the temperature of my Raspberry Pi 5. It utilizes [rye](https://rye.astral.sh/guide/installation/) to manage the virtual environment and `nohup` to ensure that the command continues running even after the terminal is closed.

## Prerequisites

- [rye 0.39.0](https://rye.astral.sh/guide/installation/)

## Installation

Clone the git repository and create the virtual environment. This step is only needed the first time.

```bash
git clone https://github.com/sche34/raspberrypi_temperature.git
cd raspberrypi_temperature
rye sync
```

## Running the Scripts

### Activate the Virtual Environment & Start the Scripts

Activate the virtual environment and start the scripts. This will store the temperature readings in `data/readings.txt`. The output of the script (not interesting) is saved in `nohup.out`.

```bash
source .venv/bin/activate

nohup run &
```

To stop the scripts, you will need to find the <i>process ID</i>. This is also returned by nohup run &. If you already have the <i>process ID</i>, skip the step below. Otherwise, write down the <i>process ID</i> that is returned by the command below and looks something like this: /home/sche34/temp_readings/.venv/bin/python3 /home/sche34/temp_readings/.venv/bin/run.
```bash
ps aux | grep python
```

Finally, stop the process:
```bash
kill <process ID>
```

