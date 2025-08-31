# Safety Rules (Klipper + Jinja)
- RESPOND MSG values must not contain raw double-curly expressions.
- Use: RESPOND MSG={"Text " ~ var|string} (string concatenation)
- Put {% if %} and {% endif %} on their own lines.
- Clamp XY commands to reachable delta radius before moves.
- Gate extrusion by min_extrude_temp (compare current vs config).
- Avoid redefining M-codes used by factory unless required.
- Keep FUI heartbeat under strict start/stop + hard reset to prevent spam.
