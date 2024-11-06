# 2D Objects Transformations

An interactive OpenGL application that allows users to manipulate and transform 2D animal shapes with smooth curve interpolation.

## Features

### Shape Collection
- Multiple pre-defined animal shapes:
  - Cat
  - Swan
  - Snail
  - Bat
  - Wolf
- Smooth curve rendering using cubic spline interpolation

### Transformations
- Translation (Movement)
  - Up (W key)
  - Down (S key)
  - Left (A key)
  - Right (D key)

- Rotation
  - Counterclockwise (Q key)
  - Clockwise (E key)

- Scaling
  - Increase size (+ key)
  - Decrease size (- key)

- Flipping
  - Horizontal flip (H key)
  - Vertical flip (V key)

### Additional Controls
- Switch between shapes
  - Next shape (N key)
  - Previous shape (P key)
- Reset shape to original position (R key)
- Exit application (ESC key)

### User Interface
- Interactive bottom menu with buttons for all operations
- Hover effects on buttons
- Clear visual feedback
- Fullscreen support

## Technical Details

### Dependencies
- Python 3.12
- PyGame
- OpenGL
- NumPy
- SciPy

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/2d-objects-transformations.git
```

2. Install required packages:
```bash
pip install pygame
```

### Running the Application
```bash
python 2d_objects_app.py
```

## Controls Summary

### Keyboard Controls
| Key | Action |
|-----|--------|
| W | Move Up |
| S | Move Down |
| A | Move Left |
| D | Move Right |
| Q | Rotate Left |
| E | Rotate Right |
| + | Scale Up |
| - | Scale Down |
| H | Flip Horizontal |
| V | Flip Vertical |
| N | Next Shape |
| P | Previous Shape |
| R | Reset Shape |
| ESC | Exit |

### Mouse Controls
- Click buttons in the bottom menu to perform actions
- Hover over buttons for visual feedback

## Implementation Details
- Built with PyGame and OpenGL for efficient 2D graphics rendering
- Uses cubic spline interpolation for smooth curve rendering
- Implements matrix transformations for precise shape manipulation
- Boundary checking to prevent shapes from leaving the visible area
- Interactive UI with clear visual feedback

## License
MIT License

Copyright (c) 2024 Olegani4

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Author
[Olegani4](https://github.com/Olegani4)

## Acknowledgments
- Thanks to the PyGame and OpenGL communities
- Inspired by classic 2D graphics manipulation tools