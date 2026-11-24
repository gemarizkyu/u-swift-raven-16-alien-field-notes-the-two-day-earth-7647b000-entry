# Alien Field Notes: The Two Day Earth Review

[![make.fun · u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/gemarizkyu/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000-entry/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/gemarizkyu/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000-entry/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

## What it does

This program writes one original alien-tourist review line (max 200
characters) to `/output/entry.txt`. The review is a field note from a
visitor rating a two-day trip to Earth.

## How to run

```sh
python3 main.py
```

The output file is created at `/output/entry.txt`. Set the `OUTPUT_DIR`
environment variable to write it somewhere else instead.

## Notes

- Python 3.13, standard library only — no network, clock, randomness,
  or model calls.
- The output is exactly one line with no trailing newline.
