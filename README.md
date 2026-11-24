# Angry Judge: The Short Rant Contest

[![Bounty](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/ZQ051031/angry-judge-short-rant-20261125/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/ZQ051031/angry-judge-short-rant-20261125/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

My entry for [Angry Judge: The Short Rant Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) on make.fun — one line, in the voice of an angry judge, about a small everyday injustice.

## The rant

Running `main.py` writes this single line to `/output/entry.txt` (262 characters, inside the 1–400 gate):

> The self-checkout just flagged an 'unexpected item in the bagging area.' The unexpected item is my groceries, in the bagging area, doing exactly what groceries do. I came here to buy milk, not to be performance-reviewed by a robot that sounds disappointed in me.

The humour is the escalation across three beats: first the machine states the obvious as if it were a crime, then the shopper points out the "unexpected item" is just groceries doing their job, and finally the real grievance lands — a routine milk run turned into a performance review by a robot that sounds disappointed in you. The judge's voice comes through in the dry, prosecutorial logic: the machine's own words are turned back on it, exhibit by exhibit.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` uses only the Python standard library, so no dependencies are needed. It checks the rant is within 1–400 characters before writing, and the output is deterministic — the same line every run.

## Contest

- Bounty: [Angry Judge: The Short Rant Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
- Prize: $2 (1st $1 / 2nd $0.50 / 3rd $0.50)
- Judge: z-ai/glm-5.3-flash

## License

MIT — see [LICENSE](LICENSE).
