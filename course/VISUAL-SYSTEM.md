# Course Visual System

The repository uses the cream direction selected for the Claude Architect Lab.
The purpose is not decoration: consistent colors help learners distinguish
inputs, evidence, decisions, successful paths, and failure paths while reading
diagrams and later reviewing the PowerPoint deck.

## Palette

| Role | Color | Use |
|---|---|---|
| Cream | `#F7F1E8` | page and diagram background |
| Navy | `#16324F` | headings, labels, primary outline |
| Blue | `#DCECF3` / `#2F6B8A` | inputs, observations, transport |
| Orange | `#F5D8C4` / `#D97941` | evidence, evaluation, attention |
| Sage | `#DCE8D8` / `#6F8F72` | pass, action, recovery |
| Red | `#F3D6D2` / `#B44B45` | failure, block, escalation |

The pale fill and dark outline are paired so the diagram remains readable on a
cream background. Red is reserved for a failure or release-blocking finding;
using it for ordinary emphasis would make a real blocker less visible.

## Diagram conventions

Use Mermaid for repository diagrams so learners can read the source and GitHub
can render the result without downloading image files.

- Blue means input, observation, transport, or context.
- Orange means evidence, evaluation, or a decision point.
- Sage means a successful action, recovery, or allowed continuation.
- Red means failure, block, unsafe behavior, or escalation.
- Navy outlines connect the visual to the course's primary text color.

Keep diagrams focused on one relationship. If a diagram needs more than seven
major nodes, split it into two diagrams rather than shrinking the labels until
the learner cannot read them.

## Slide translation

The same roles should carry into the PowerPoint deck:

- cream slide background;
- navy headings and body text;
- orange for the evaluation decision;
- blue for the workflow or input;
- sage for a passing or recovered path;
- red for a deliberately degraded case or blocking finding.

The deck may use a darker panel for a screen demo, but that panel is a demo
container, not a second course theme.
