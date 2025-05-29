# Epic-Sans
## Project Overview

**Epic!Sans Fight** is a video game developed in Python using the Pygame library. It is a *boss fight* style game inspired by the universe of **Undertale**, where the player faces a character named *Sans* through a series of intense and varied attack phases. In this boss fight, the player does not face Sans, but *Epic!Sans*, a character from the alternate universe of Undertale, **Epictale**. The specificity of this character is that he has "memes" and "anime" powers. This game therefore presents some of these abilities.

This project was created as a way to practice object-oriented programming, real-time event management, and the implementation of complex game mechanics (collisions, animations, sound effects, etc.).

---

## General Functionality

The game is based on a main loop that handles user inputs, updates game objects, and draws all elements to the screen. It is composed of multiple classes, each with specific responsibilities:

* **`Player`**: Manages movement, jumping, gravity (in some phases), collisions, and the soul’s state.
* **`Epic_sans`**: Controls the opponent's animations and visual effects.
* **`Attacks`**: Orchestrates the timeline of attacks (Gaster Blasters, bones, platforms, special effects...).
* **`GasterBlaster`, `Bones`, `TimeStopManager`, `Kamehameha`, etc.**: Handle different kinds of special attack mechanics.
* **`Box`**: Controls the combat area and its dynamic resizing during phases.
* **`HP`**: Manages health, Karma damage over time, and the game-over sequence.
* **`Menu`, `Intro`, `Decorations`, `End`**: Handle the menu system, intro sequence, end screen, and UI visuals.

---

## Controls

| Key          | Action                                                |
| ------------ | ----------------------------------------------------- |
| `Arrow Keys` | Move the soul (left/right/up/down depending on state) |
| `Z`          | Confirm in menus                                      |
| `X`          | Cancel or go back in menus                            |
| `E`          | Enable debug mode                                     |
| `D`          | Disable debug mode                                    |

---

## Game Mechanics

Here are some essential mechanics that define the gameplay and challenge:

### Bone Colors
* **White Bones**: Normal damage if touched.

* **Blue Bones**: Only hurt you if you're moving when touching them.
→ To avoid damage, stay still.

* **Orange Bones**: Only hurt you if you're not moving when touching them.
→ To avoid damage, keep moving.

### Blue Soul (Gravity Mode)
At certain points, your soul will turn **blue**, enabling **gravity mechanics**:

* Your soul will be pulled in a direction (down, up, left, or right).

* You can **jump** using directional keys (e.g., UP or LEFT, depending on gravity).

* You’ll also need to land or stay on **moving platforms** to survive.

### Time Stop Effect
* During a special phase, time will "stop", and a **dark overlay** will appear.

* Despite appearances, attacks still continue, so you must stay alert.

### Fake Gaster Blasters
* Some "fake" blasters cause a **brief black screen** and play a sound.

* These do not deal damage but are meant to distract and disorient.

### Audio Cues
* Each attack type has its own **sound effects** that serve as warnings.

* For example, Gaster Blasters charge with a specific noise before firing.

---

## Learning Objectives

This project allowed me to:

* Strengthen my understanding of **object-oriented programming**.
* Learn how to structure a **complex game project using Pygame**.
* Implement **advanced timing**, **collision detection**, and **custom gravity mechanics**.
* Handle **multimedia assets** efficiently (images, sound effects, music).
* Build an **interactive menu system** and manage state transitions and animations over time.

---

## How to Run

1. Make sure you have **Python** and **Pygame** installed:

   ```bash
   pip install pygame pygame-menu
   ```
2. Launch the game with:

   ```bash
   python main.py
   ```

The game will start with an interactive menu that lets you begin the fight.

---

## Notes

* All assets (sounds, images, fonts) are located in the `assets/` directory.
* The goal of the game is to **survive** the full sequence of attacks.
* This project is **non-commercial** and was developed purely for educational purposes.

---

## Credits

* **Undertale:** Toby Fox
* **Epictale:** Yugogeer012
* **Jojo's Bizarre Adventure:** Hirohiko Araki
* **Dragon Ball:** Akira Toriyama
* **Epic Sans, Gaster Blasters, light balls, floating chicken sprites:** dahifhadf
* **Dio's road roller sprite:** JoJo's Bizarre Adventure: Heritage for the Future
* **Star Platinium's fist sprite:** souyu
* **"The End" message sprite:** Font Meme
* **"PLOT ARMOR" theme:** Box Standard
* **"Bruh" theme:** NyxTheShield
