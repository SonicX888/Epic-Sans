# --- Class: Bones ---
# Purpose: Represents a single bone object (or platform) that moves from a start to an end position, possibly reversing
import pygame
import time

class Bones:
    def __init__(self, image, start_x, start_y, end_x, end_y, speed, start_time, platform, blue, orange, reverse=False):
        # Store image and initial/final coordinates
        self.image = image
        self.x = start_x
        self.y = start_y
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

        # Speed and activation timing
        self.speed = speed
        self.start_time = start_time
        self.active = False  # Flag to indicate if the bone is active

        # Bone behavior flags
        self.platform = platform  # True if bone acts as a platform
        self.reversed = reverse  # If True, bone will return to start
        self.blue = blue  # Special interaction
        self.orange = orange  # Special interaction
        self.returning = False  # State flag if returning

        self._set_direction(start_x, start_y, end_x, end_y)  # Calculate direction vector

        self.visible = False  # Initially invisible until activated

    def _set_direction(self, from_x, from_y, to_x, to_y):
        # Calculate and normalize the direction vector for movement
        dx = to_x - from_x
        dy = to_y - from_y
        distance = (dx**2 + dy**2) ** 0.5
        if distance == 0:
            self.direction_x, self.direction_y = 0, 0
        else:
            self.direction_x = dx / distance
            self.direction_y = dy / distance

    def update(self):
        # Manage activation delay
        if not self.active:
            if time.time() >= self.start_time:
                self.active = True
            else:
                return False

        # Update position based on direction and speed
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed

        # Determine current target
        target_x = self.end_x if not self.returning else self.start_x
        target_y = self.end_y if not self.returning else self.start_y

        # Check if bone has reached target position
        if ((self.direction_x >= 0 and self.x >= target_x) or
            (self.direction_x < 0 and self.x <= target_x)) and \
           ((self.direction_y >= 0 and self.y >= target_y) or
            (self.direction_y < 0 and self.y <= target_y)):
            # Snap to target to prevent overshoot
            self.x = target_x
            self.y = target_y

            # Handle return if reversed
            if self.reversed and not self.returning:
                self.returning = True
                self._set_direction(self.x, self.y, self.start_x, self.start_y)
                return False  # Still in progress
            return True  # Reached destination and no return

        return False  # Still moving

    def draw(self, surface):
        if self.active or self.visible:
            self.rect = self.image.get_rect(center=(self.x, self.y))
            surface.blit(self.image, self.rect)
