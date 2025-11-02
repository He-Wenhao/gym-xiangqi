import os
import pygame

# Enable verbose SDL output
os.environ['SDL_DEBUG'] = '1'

print("Available audio drivers:")
for driver in ['pulseaudio', 'alsa', 'dsp', 'esd']:
    os.environ['SDL_AUDIODRIVER'] = driver
    try:
        pygame.mixer.init()
        print(f"  ✓ {driver} works!")
        pygame.mixer.quit()
    except pygame.error as e:
        print(f"  ✗ {driver} failed: {e}")