# --- Class: Accessory ---
# Purpose: Manages special visual elements that orbit or oscillate around Epic!Sans for cinematic effects
import math

class Accessory:
    def __init__(self, image, kind, center_y):
        self.image = image          # The accessory image surface
        self.kind = kind            # Type of motion: 'oval', 'oval_low', 'oscillate'
        self.center_y = center_y    # Vertical center reference
        self.width = 1000           # Width of orbital/oscillation range
        self.height = 150           # Height of the oval path
        self.center_x = 500         # Horizontal center reference
        self.finished = False       # Whether the motion is complete
        self.exiting = False        # Whether the accessory is leaving the screen

        # Oscillation and oval motion parameters
        self.osc_freq = 2
        self.osc_amp = self.width // 2
        self.vert_freq = 10
        self.vert_amp = 15

        # Initial phase and position
        if self.kind == "oscillate":
            start_x = -200
            ratio = (self.center_x - start_x) / self.osc_amp
            ratio = max(-1, min(1, ratio))
            self.t_phase = -math.asin(ratio) / self.osc_freq
            self.pos = [start_x, center_y]
        else:
            self.t_phase = 0
            self.pos = [-100, center_y]

    def update(self, hp, stop):

        if hp > 0:

            if not stop:

                # Advance the time phase each frame
                self.t_phase += 1 / 60

                if self.exiting:
                    # Move right when exiting
                    self.pos[0] += 8
                    if self.pos[0] > 1200:
                        self.finished = True
                    return

                if self.kind in ["oval", "oval_low"]:
                    # Calculate elliptical orbit position
                    t = self.t_phase * 4
                    x = self.center_x + math.cos(t) * (self.width // 2)
                    y = self.center_y + math.sin(t) * (self.height // 2)
                    self.pos = [x, y]

                    # Mark as exiting after full loop
                    if t >= 2 * math.pi:
                        self.exiting = True

                elif self.kind == "oscillate":
                    # Oscillate back and forth with vertical bobbing
                    t = self.t_phase
                    x = self.center_x + math.sin(t * self.osc_freq) * self.osc_amp
                    y = self.center_y + math.sin(t * self.vert_freq) * self.vert_amp
                    self.pos = [x, y]
