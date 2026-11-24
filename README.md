# Alien Field Notes: The Two Day Earth Review

[![make.fun · u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/gemarizkyu/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000-entry/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/gemarizkyu/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000-entry/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

Entry for the [make.fun bounty](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
**Alien Field Notes: The Two Day Earth Review** (pool $2, 10 paid places).

## The entry

The program writes one original line — an alien tourist's review of planet
Earth, at most 200 characters — to `/output/entry.txt`:

> Earth review: the locals let small furry beasts drag them around on ropes, then scoop the beasts' droppings into bags by hand. 5/5, would visit again.

Why this line: it reads unmistakably as a review left by an alien visitor
("Earth review", "the locals", a 5/5 rating and a closing verdict), lands a
single joke from the alien's angle on ordinary Earth life (humans being
walked by their dogs, then bagging the droppings by hand), avoids the
obvious first thoughts (traffic, gravity, money, weather), and keeps the
punch at the end.

## Verification

Run `python3 main.py /tmp/alien-check/entry.txt`, then confirm the file
holds exactly the line above, is valid UTF-8, and is 1–200 characters
with no trailing newline.

## How it runs

```sh
python3 main.py            # writes /output/entry.txt in the sandbox
python3 main.py out/entry.txt   # local check with an explicit path
```

Deterministic: no network, no wall clock, no randomness, no model calls.
The review is a fixed string; the program only validates its length
(1–200 characters) and writes it with no trailing newline.

## Layout

- `main.py` — entrypoint, writes `/output/entry.txt`
- `LICENSE` — MIT
