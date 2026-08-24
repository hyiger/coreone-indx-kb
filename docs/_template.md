---
title:        # Short, searchable. What someone would type.
confidence:   # measured | reported | provisional
updated:      # YYYY-MM-DD
author:       # hyiger

# Hardware this applies to. Be specific — a value that holds on a 0.4mm
# Diamondback may not hold on a 0.6mm CHT. "unknown" is allowed; blank is not.
printer:      # Core One | Core One L | H2D | ...
toolhead:     # INDX | single | ...
hotend:       # E3D Diamondback | CHT | Revo | ...
nozzle:       # 0.4mm | 0.6mm | ...
firmware:     # version string, or unknown

# Where this came from. Required for reported/provisional.
sources:
  # - https://forum.prusa3d.com/...

# Set when this stops being true. Do not delete the page.
superseded_by:
---

# Title

## Summary

One paragraph. What is the finding, stated plainly. A reader should be able to
stop here and have the answer.

## Detail

Why it happens, what to check, what to do. Your own words — if you are working
from a forum thread, extract the finding and link the thread rather than
reproducing the post.

## Verification

For `measured`: how was this tested? What did you run, on what hardware, what
did you observe? Someone should be able to repeat it.

For `reported`: link the independent reports. Note where they disagree.

For `provisional`: say plainly that this is one person's experience and has not
been reproduced.

## Related

Links to other pages here.
