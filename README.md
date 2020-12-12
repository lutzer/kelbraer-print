# kelbraer-print

## Raspberry Pi Setup

* hostname: *kelbraerpi.local*
* `sudo raspi-config`
  * Interface Options -> Serial Port: disable login shell, enable serial interface

* update packages:
  ```
  sudo apt-get update
  sudo apt-get install git cups wiringpi build-essential libcups2-dev libcupsimage2-dev python-serial python-pil python-unidecode
  ```
* install printer drivers:
  ```
  git clone https://github.com/adafruit/zj-58
  cd zj-58
  make
  sudo ./install
  ```

## Development

* create virtual environment : python3 -m venv .venv
* activate source .venv/bin/activate (deactivate to exit)