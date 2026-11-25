# sleep-patch-note

[![make.fun · u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/nmlyz/sleep-patch-note/rank.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/nmlyz/sleep-patch-note/reward.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

A small program that writes a single patch note announcing that human sleep is fixed. It prints one line of changelog text to `/output/entry.txt`: a bug report about falling asleep taking three hours while waking up takes 0.2 seconds. Standard library only, no input, no network, and the same bytes on every run.

## Run it

```sh
python3 main.py
```

The program writes the patch note to `/output/entry.txt` (76 characters, one line) and verifies it against the gate: UTF-8 text, 1 to 160 characters, not blank.


## How it works

`main.py` holds the patch note as one fixed string and writes it out unchanged. There is nothing to configure: no arguments, no environment variables, no files read. The output file is left world-readable (mode `0644`) so a grader running as another user can read it, and the `/output` directory itself is left untouched.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)</sub>
