import pygame as pg
from OpenGL.GL import *
import numpy as np
from scipy.interpolate import CubicSpline


def get_cat_vertices(scale_factor=0.5):
    sf = scale_factor
    vertices = [
        -0.2 * sf, 0.3 * sf, 0.0, 
        -0.3 * sf, 0.5 * sf, 0.0, 
        -0.4 * sf, 0.6 * sf, 0.0, 
        -0.4 * sf, 0.7 * sf, 0.0, 
        -0.6 * sf, 0.7 * sf, 0.0, 
        -0.4 * sf, 0.8 * sf, 0.0, 
        -0.5 * sf, 0.8 * sf, 0.0, 
        -0.2 * sf, 1.0 * sf, 0.0, 
        0.1 * sf, 1.0 * sf, 0.0,  
        0.6 * sf, 0.4 * sf, 0.0,  
        0.6 * sf, 0.0 * sf, 0.0,  
        0.5 * sf, -0.5 * sf, 0.0, 
        0.5 * sf, -0.8 * sf, 0.0, 
        0.6 * sf, -0.9 * sf, 0.0, 
        0.5 * sf, -1.0 * sf, 0.0, 
        0.4 * sf, -0.9 * sf, 0.0, 
        0.35 * sf, -0.4 * sf, 0.0,
        0.3 * sf, -0.9 * sf, 0.0, 
        0.4 * sf, -1.0 * sf, 0.0, 
        0.2 * sf, -1.0 * sf, 0.0, 
        0.1 * sf, -0.2 * sf, 0.0, 
        0.1 * sf, -0.6 * sf, 0.0, 
        0.0 * sf, -0.8 * sf, 0.0, 
        0.1 * sf, -0.9 * sf, 0.0, 
        0.0 * sf, -1.0 * sf, 0.0, 
        -0.4 * sf, -1.0 * sf, 0.0,
        -0.7 * sf, -0.8 * sf, 0.0,
        -1.1 * sf, -0.8 * sf, 0.0,
        -1.1 * sf, -0.9 * sf, 0.0,
        -0.8 * sf, -1.0 * sf, 0.0,
        -0.5 * sf, -1.0 * sf, 0.0,
        -0.4 * sf, -1.1 * sf, 0.0,
        -0.8 * sf, -1.1 * sf, 0.0,
        -1.3 * sf, -1.0 * sf, 0.0,
        -1.2 * sf, -0.7 * sf, 0.0,
        -0.7 * sf, -0.7 * sf, 0.0,
        -0.6 * sf, -0.2 * sf, 0.0,
        -0.4 * sf, -0.1 * sf, 0.0,
        -0.2 * sf, 0.2 * sf, 0.0, 
        0.0 * sf, 0.4 * sf, 0.0,  
        -0.1 * sf, 0.5 * sf, 0.0, 
        -0.2 * sf, 0.3 * sf, 0.0, 
    ]
    color = (1.0, 0.5, 0.0)  # Orange for cat
    return vertices, color

def get_swan_vertices(scale_factor=0.5):
    sf = scale_factor
    vertices = [
        -1.0 * sf, 0.6 * sf, 0.0, 
        -0.95 * sf, 0.8 * sf, 0.0,
        -0.8 * sf, 1.0 * sf, 0.0, 
        -0.7 * sf, 1.0 * sf, 0.0, 
        -0.6 * sf, 0.9 * sf, 0.0, 
        -0.6 * sf, 0.7 * sf, 0.0, 
        -0.7 * sf, 0.3 * sf, 0.0, 
        -0.7 * sf, 0.1 * sf, 0.0, 
        -0.6 * sf, 0.2 * sf, 0.0, 
        -0.4 * sf, 0.3 * sf, 0.0, 
        0.5 * sf, 0.3 * sf, 0.0,  
        0.3 * sf, 0.1 * sf, 0.0,  
        0.7 * sf, 0.3 * sf, 0.0,  
        0.7 * sf, 0.2 * sf, 0.0,  
        0.6 * sf, 0.1 * sf, 0.0,  
        0.7 * sf, 0.1 * sf, 0.0,  
        0.5 * sf, -0.1 * sf, 0.0, 
        0.7 * sf, -0.1 * sf, 0.0, 
        1.0 * sf, 0.0 * sf, 0.0,  
        0.8 * sf, -0.3 * sf, 0.0, 
        0.4 * sf, -0.4 * sf, 0.0, 
        0.0 * sf, -0.4 * sf, 0.0, 
        -0.4 * sf, -0.3 * sf, 0.0,
        -0.9 * sf, -0.4 * sf, 0.0,
        -1.0 * sf, -0.3 * sf, 0.0,
        -1.0 * sf, 0.0 * sf, 0.0, 
        -0.7 * sf, 0.7 * sf, 0.0, 
        -0.7 * sf, 0.8 * sf, 0.0, 
        -0.8 * sf, 0.7 * sf, 0.0, 
        -0.9 * sf, 0.7 * sf, 0.0, 
        -1.0 * sf, 0.6 * sf, 0.0, 
    ]
    color = (1.0, 1.0, 1.0)  # White for swan
    return vertices, color

def get_snail_vertices(scale_factor=0.5):
    sf = scale_factor
    vertices = [
        # Main body
        -0.2 * sf, 0.0 * sf, 0.0, 
        -0.3 * sf, -0.1 * sf, 0.0,
        0.3 * sf, -0.1 * sf, 0.0, 
        0.5 * sf, 0.1 * sf, 0.0,  
        0.6 * sf, 0.3 * sf, 0.0,  
        0.7 * sf, 0.3 * sf, 0.0,  
        0.8 * sf, 0.4 * sf, 0.0,  
        0.8 * sf, 0.5 * sf, 0.0,  
        0.7 * sf, 0.6 * sf, 0.0,  
        0.8 * sf, 0.8 * sf, 0.0,  
        0.7 * sf, 0.8 * sf, 0.0,  
        0.7 * sf, 0.6 * sf, 0.0,  
        0.6 * sf, 0.6 * sf, 0.0,  
        0.6 * sf, 0.8 * sf, 0.0,  
        0.5 * sf, 0.8 * sf, 0.0,  
        0.6 * sf, 0.6 * sf, 0.0,  
        0.5 * sf, 0.5 * sf, 0.0,  
        0.5 * sf, 0.4 * sf, 0.0,  
        0.3 * sf, 0.2 * sf, 0.0,  
        0.4 * sf, 0.5 * sf, 0.0,  
        0.4 * sf, 0.7 * sf, 0.0,  
        0.2 * sf, 0.9 * sf, 0.0,  
        -0.1 * sf, 0.9 * sf, 0.0, 
        -0.4 * sf, 0.7 * sf, 0.0, 
        -0.5 * sf, 0.4 * sf, 0.0, 
        -0.4 * sf, 0.2 * sf, 0.0, 
        -0.2 * sf, 0.0 * sf, 0.0, 
        0.0 * sf, 0.0 * sf, 0.0,  
        0.2 * sf, 0.2 * sf, 0.0,  
        0.2 * sf, 0.5 * sf, 0.0,  
        0.1 * sf, 0.7 * sf, 0.0,  
        -0.1 * sf, 0.7 * sf, 0.0, 
        -0.2 * sf, 0.5 * sf, 0.0, 
        -0.2 * sf, 0.3 * sf, 0.0, 
        0.0 * sf, 0.2 * sf, 0.0,  
        0.1 * sf, 0.3 * sf, 0.0,  
        0.0 * sf, 0.4 * sf, 0.0,  
    ]
    color = (0.0, 1.0, 0.0)  # Green for snail
    return vertices, color

def get_bat_vertices(scale_factor=0.5):
    sf = scale_factor
    vertices = [
        3 * sf, 3 * sf, 0.0,
        5 * sf, -1 * sf, 0.0,
        6 * sf, -2 * sf, 0.0,
        8 * sf, 0 * sf, 0.0,
        10 * sf, 4 * sf, 0.0,
        12 * sf, 8 * sf, 0.0,
        13 * sf, 12 * sf, 0.0,
        13 * sf, 16 * sf, 0.0,
        15 * sf, 15 * sf, 0.0,
        19 * sf, 15 * sf, 0.0,
        22 * sf, 15 * sf, 0.0,
        24 * sf, 15 * sf, 0.0,
        26 * sf, 16 * sf, 0.0,
        25 * sf, 14 * sf, 0.0,
        23 * sf, 10 * sf, 0.0,
        22 * sf, 6 * sf, 0.0,
        19 * sf, 5 * sf, 0.0,
        17 * sf, 3 * sf, 0.0,
        16 * sf, 1 * sf, 0.0,
        15 * sf, -3 * sf, 0.0,
        15 * sf, -7 * sf, 0.0,
        13 * sf, -8 * sf, 0.0,
        11 * sf, -10 * sf, 0.0,
        9 * sf, -12 * sf, 0.0,
        8 * sf, -14 * sf, 0.0,
        7 * sf, -18 * sf, 0.0,
        5 * sf, -16 * sf, 0.0,
        1 * sf, -14 * sf, 0.0,
        0 * sf, -14 * sf, 0.0,
        -4 * sf, -15 * sf, 0.0,
        -6 * sf, -17 * sf, 0.0,
        -8 * sf, -15 * sf, 0.0,
        -10 * sf, -13 * sf, 0.0,
        -11 * sf, -12 * sf, 0.0,
        -12 * sf, -12 * sf, 0.0,
        -13 * sf, -12 * sf, 0.0,
        -14 * sf, -13 * sf, 0.0,
        -17 * sf, -15 * sf, 0.0,
        -18 * sf, -15 * sf, 0.0,
        -22 * sf, -13 * sf, 0.0,
        -24 * sf, -12 * sf, 0.0,
        -25 * sf, -12 * sf, 0.0,
        -27 * sf, -13 * sf, 0.0,
        -25 * sf, -11 * sf, 0.0,
        -23 * sf, -8 * sf, 0.0,
        -21 * sf, -5 * sf, 0.0,
        -19 * sf, 0 * sf, 0.0,
        -15 * sf, -2 * sf, 0.0,
        -12 * sf, -4 * sf, 0.0,
        -10 * sf, -5 * sf, 0.0,
        -7 * sf, -6 * sf, 0.0,
        -4 * sf, -6 * sf, 0.0,
        -1 * sf, -6 * sf, 0.0,
        -1 * sf, -3 * sf, 0.0,
        -2 * sf, 1 * sf, 0.0,
        0 * sf, -1 * sf, 0.0,
        1 * sf, 0 * sf, 0.0,
        2 * sf, 0 * sf, 0.0,
        3 * sf, 1 * sf, 0.0,
        3 * sf, 3 * sf, 0.0,
    ]
    color = (0.0, 0.0, 0.0)  # Black for bat
    return vertices, color

def get_wolf_vertices(scale_factor=0.5):
    sf = scale_factor
    vertices = [
        7 * sf, -3 * sf, 0.0,
        8 * sf, -2 * sf, 0.0,
        7 * sf, 2 * sf, 0.0,
        5 * sf, 3 * sf, 0.0,
        2 * sf, 2 * sf, 0.0,
        -1 * sf, 3 * sf, 0.0,
        -3 * sf, 4 * sf, 0.0,
        -5 * sf, 6 * sf, 0.0,
        -5 * sf, 7 * sf, 0.0,
        -6 * sf, 6 * sf, 0.0,
        -7 * sf, 6 * sf, 0.0,
        -7.5 * sf, 5.5 * sf, 0.0,
        -10 * sf, 5.5 * sf, 0.0,
        -9.5 * sf, 4.5 * sf, 0.0,
        -7 * sf, 4 * sf, 0.0,
        -5 * sf, 2 * sf, 0.0,
        -5 * sf, 0 * sf, 0.0,
        -4 * sf, -2 * sf, 0.0,
        -4 * sf, -5.5 * sf, 0.0,
        -5 * sf, -6.5 * sf, 0.0,
        -4 * sf, -6.5 * sf, 0.0,
        -3 * sf, -5.5 * sf, 0.0,
        -3 * sf, -3 * sf, 0.0,
        -2 * sf, -2 * sf, 0.0,
        -2 * sf, -1 * sf, 0.0,
        1 * sf, -1 * sf, 0.0,
        3.5 * sf, -0.5 * sf, 0.0,
        5 * sf, -2 * sf, 0.0,
        6 * sf, -5.5 * sf, 0.0,
        5 * sf, -6.5 * sf, 0.0,
        6 * sf, -6.5 * sf, 0.0,
        7 * sf, -5.5 * sf, 0.0,
        6.5 * sf, -2.5 * sf, 0.0,
        7 * sf, -1 * sf, 0.0,
        7 * sf, 0 * sf, 0.0,
    ]
    color = (0.5, 0.5, 0.5)  # Gray for wolf
    return vertices, color


class App:
    def __init__(self, width=1280, height=720, fullscreen=False, title="App", figure_vertices=None, figure_colors=None):
        # Initialize pygame
        pg.init()

        # Set name of the window
        pg.display.set_caption(title)

        # Get the screen info for fullscreen
        screen_info = pg.display.Info()
        if width and height:
            self.width = width
            self.height = height
        else:
            self.width = screen_info.current_w
            self.height = screen_info.current_h

        if fullscreen:
            # Create the fullscreen window
            pg.display.set_mode((self.width, self.height), flags=pg.OPENGL|pg.DOUBLEBUF|pg.FULLSCREEN)
        else:
            # Create the windowed window
            pg.display.set_mode((self.width, self.height), flags=pg.OPENGL|pg.DOUBLEBUF)
            
        self.clock = pg.time.Clock()

        # Initialize OpenGL
        glClearColor(0.1, 0.2, 0.2, 1.0)

        # Store all figures and current figure index
        self.figures_vertices = figure_vertices  # Now expecting a list of vertices
        self.current_figure_index = 0
        self.figure_colors = figure_colors

        # Create initial figure
        if self.figures_vertices:
            self.figure = Figure(self.figures_vertices[0], self.figure_colors[0])
            self.figure.app = self

        # Add menu initialization after figure creation
        self.menu = BottomMenu(self.width, self.height, self)

        self.main_loop()

    def main_loop(self):
        running = True
        while running:
            # Handle mouse position for hover effects
            mouse_pos = pg.mouse.get_pos()
            self.menu.handle_mouse(mouse_pos)

            for event in pg.event.get():
                if (event.type == pg.QUIT) or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    print('Exit')
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        print('Restore')
                        self.figure.restore()
                    elif event.key == pg.K_n:
                        self.next_figure()
                    elif event.key == pg.K_p:
                        self.prev_figure()
                    elif event.key == pg.K_h:  # Add horizontal flip
                        print('Flip horizontal')
                        self.figure.flip_horizontal()
                    elif event.key == pg.K_v:  # Add vertical flip
                        print('Flip vertical')
                        self.figure.flip_vertical()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        self.menu.handle_click(pg.mouse.get_pos(), self.figure)

            # Get the current state of all keyboard buttons
            keys = pg.key.get_pressed()

            # Check for held keys and apply continuous movement/rotation/scaling
            if keys[pg.K_w]:
                print('Move up')
                self.figure.translate(0, 0.02)
            if keys[pg.K_s]:
                print('Move down')
                self.figure.translate(0, -0.02)
            if keys[pg.K_a]:
                print('Move left')
                self.figure.translate(-0.02, 0)
            if keys[pg.K_d]:
                print('Move right')
                self.figure.translate(0.02, 0)
            if keys[pg.K_q]:
                print('Rotate counterclockwise')
                self.figure.rotate(-5)
            if keys[pg.K_e]:
                print('Rotate clockwise')
                self.figure.rotate(5)
            if keys[pg.K_EQUALS] or keys[pg.K_KP_PLUS]:  # Both + and numpad +
                print('Scale up')
                self.figure.scale(1.02)
            if keys[pg.K_MINUS] or keys[pg.K_KP_MINUS]:  # Both - and numpad -
                print('Scale down')
                self.figure.scale(0.98)
                
            # Clear screen
            glClear(GL_COLOR_BUFFER_BIT)
            
            # Set up projection for the figure
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(-1, 1, -1, 1, -1, 1)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            
            # Draw cat figure
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
            glColor3f(*self.figure.color)
            self.figure.draw()

            # Draw menu (this will set up its own projection)
            self.menu.draw()
            
            pg.display.flip()
            self.clock.tick(60)
        self.quit()  # Quit the application

    def quit(self):
        self.figure.destroy()  # Delete the figure
        pg.quit()  # Quit the application
        
    def next_figure(self):
        if self.figures_vertices:
            # Update index
            self.current_figure_index = (self.current_figure_index + 1) % len(self.figures_vertices)
            # Clean up old figure
            self.figure.destroy()
            # Create new figure
            self.figure = Figure(self.figures_vertices[self.current_figure_index], self.figure_colors[self.current_figure_index])
            self.figure.app = self

    def prev_figure(self):
        if self.figures_vertices:
            # Update index
            self.current_figure_index = (self.current_figure_index - 1) % len(self.figures_vertices)
            # Clean up old figure
            self.figure.destroy()
            # Create new figure
            self.figure = Figure(self.figures_vertices[self.current_figure_index], self.figure_colors[self.current_figure_index])
            self.figure.app = self

class Figure:
    def __init__(self, vertices, color):
        # Convert input vertices to numpy array if not already
        self.vertices = np.array(vertices, dtype=np.float32)
        self.vertex_count = len(self.vertices) // 3  # Number of vertices
        self.color = color

        self.vao = glGenVertexArrays(1)  # Vertex Array Object
        glBindVertexArray(self.vao)

        self.vbo = glGenBuffers(1)  # Vertex Buffer Object
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))

        # Store initial vertices for restoration
        self.initial_vertices = np.copy(self.vertices)

        # Add new attribute for interpolation points
        self.spline_points = self.generate_spline_points()

    def generate_spline_points(self, num_points=500):
        """Generate smooth points using cubic spline interpolation"""
        vertices_reshaped = self.vertices.reshape(-1, 3)
        
        # Add the first point at the end to close the loop
        vertices_loop = np.vstack((vertices_reshaped, vertices_reshaped[0]))
        
        # Create parameter t with uniform spacing
        t = np.linspace(0, 1, len(vertices_loop))
        
        # Create splines for x, y coordinates with periodic boundary conditions
        cs_x = CubicSpline(t, vertices_loop[:, 0])
        cs_y = CubicSpline(t, vertices_loop[:, 1])
        
        # Generate smooth points
        t_new = np.linspace(0, 1, num_points)
        x_smooth = cs_x(t_new)
        y_smooth = cs_y(t_new)
        z_smooth = np.zeros_like(x_smooth)
        
        return np.column_stack((x_smooth, y_smooth, z_smooth)).astype(np.float32)

    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))

    def draw(self):
        glBindVertexArray(self.vao)
        
        # Update buffer with spline points
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.spline_points.nbytes, self.spline_points, GL_STATIC_DRAW)
        
        # Draw only the smooth curve
        glDrawArrays(GL_LINE_STRIP, 0, len(self.spline_points))

    def rotate(self, angle):
        # Convert angle to radians
        angle_rad = np.radians(angle)
        
        # Reshape vertices into (N, 3) matrix where N is number of vertices
        vertices_reshaped = self.vertices.reshape(-1, 3)
        
        # Create rotation matrix
        rotation_matrix = np.array([
            [np.cos(angle_rad), -np.sin(angle_rad), 0],
            [np.sin(angle_rad), np.cos(angle_rad), 0],
            [0, 0, 1]
        ])
        
        # Calculate new positions after rotation
        rotated_vertices = vertices_reshaped @ rotation_matrix
        
        # Check if rotation would put any vertex outside bounds
        if not self.is_within_bounds(rotated_vertices):
            return  # Skip the rotation if it would go out of bounds
        
        # Update vertices and buffer data
        self.vertices = rotated_vertices.flatten().astype(np.float32)  # Ensure float32 type
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferSubData(GL_ARRAY_BUFFER, 0, self.vertices.nbytes, self.vertices)  # Use glBufferSubData instead

        # Update spline points after rotation
        self.spline_points = self.generate_spline_points()

    def scale(self, scale_factor):
        # Reshape vertices into (N, 3) matrix where N is number of vertices
        vertices_reshaped = self.vertices.reshape(-1, 3)
        
        # Calculate new positions
        scaled_vertices = vertices_reshaped * scale_factor
        
        # Check if scaling would put any vertex outside bounds
        if not self.is_within_bounds(scaled_vertices):
            return  # Skip the scaling if it would go out of bounds
        
        # Update vertices and buffer data
        self.vertices = scaled_vertices.flatten().astype(np.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferSubData(GL_ARRAY_BUFFER, 0, self.vertices.nbytes, self.vertices)

        # Update spline points after scaling
        self.spline_points = self.generate_spline_points()

    def translate(self, dx, dy):
        # Reshape vertices into (N, 3) matrix where N is number of vertices
        vertices_reshaped = self.vertices.reshape(-1, 3)
        
        # Create translation matrix
        translation = np.array([dx, dy, 0])
        
        # Calculate new positions
        translated_vertices = vertices_reshaped + translation
        
        # Check if translation would put any vertex outside bounds
        if not self.is_within_bounds(translated_vertices):
            return  # Skip the translation if it would go out of bounds
        
        # Update vertices and buffer data
        self.vertices = translated_vertices.flatten().astype(np.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferSubData(GL_ARRAY_BUFFER, 0, self.vertices.nbytes, self.vertices)

        # Update spline points after translation
        self.spline_points = self.generate_spline_points()

    def restore(self):
        # Restore vertices to initial state
        self.vertices = np.copy(self.initial_vertices)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferSubData(GL_ARRAY_BUFFER, 0, self.vertices.nbytes, self.vertices)

        # Update spline points after restoration
        self.spline_points = self.generate_spline_points()

    def is_within_bounds(self, new_vertices):
        # Reshape to get individual vertex coordinates
        vertices_reshaped = new_vertices.reshape(-1, 3)
        
        # Check if any vertex would go outside the bounds
        x_coords = vertices_reshaped[:, 0]
        y_coords = vertices_reshaped[:, 1]
        
        # Convert menu height to OpenGL coordinates (0 to 1 scale)
        menu_height_gl = (120 / self.app.height) * 2  # Convert pixels to GL coordinates
        
        # OpenGL viewport bounds are -1 to 1, but bottom is restricted by menu
        return (np.all(x_coords >= -1) and np.all(x_coords <= 1) and 
                np.all(y_coords >= -1 + menu_height_gl) and np.all(y_coords <= 1))

    def flip_vertical(self):
        # Reshape vertices into (N, 3) matrix
        vertices_reshaped = self.vertices.reshape(-1, 3)
        
        # Flip x coordinates
        vertices_reshaped[:, 0] = -vertices_reshaped[:, 0]
        
        # Update vertices and buffer data
        self.vertices = vertices_reshaped.flatten().astype(np.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferSubData(GL_ARRAY_BUFFER, 0, self.vertices.nbytes, self.vertices)

        # Update spline points after flipping
        self.spline_points = self.generate_spline_points()

    def flip_horizontal(self):
        # Reshape vertices into (N, 3) matrix
        vertices_reshaped = self.vertices.reshape(-1, 3)
        
        # Flip y coordinates
        vertices_reshaped[:, 1] = -vertices_reshaped[:, 1]
        
        # Update vertices and buffer data
        self.vertices = vertices_reshaped.flatten().astype(np.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferSubData(GL_ARRAY_BUFFER, 0, self.vertices.nbytes, self.vertices)

        # Update spline points after flipping
        self.spline_points = self.generate_spline_points()

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.action = action
        
        # Special color for exit button, default green for others
        if action == "exit":
            self.color = (0.8, 0.2, 0.2)  # Light red for exit
            self.hover_color = (0.9, 0.3, 0.3)  # Slightly lighter red for hover
        else:
            self.color = (0.2, 0.7, 0.2)  # Default green
            self.hover_color = (0.3, 0.8, 0.3)  # Slightly lighter green for hover
            
        self.is_hovered = False

class BottomMenu:
    def __init__(self, window_width, window_height, app=None):
        self.window_width = window_width
        self.window_height = window_height
        self.menu_height = 120
        self.button_width = 150
        self.button_height = 40
        self.padding = 10
        self.app = app
        # Initialize pygame font
        pg.font.init()
        self.font = pg.font.Font(None, 30)
        self.buttons = self.create_buttons()

    def create_buttons(self):
        buttons = []
        
        # Define buttons for each column and row
        left_column_configs = [
            # Row 1
            [
                ("^ (W)", "move_up"),
                ("v (S)", "move_down"),
                ("< (A)", "move_left"),
                ("> (D)", "move_right"),
                ("Flip ver. (V)", "flip_vertical"),
            ],
            # Row 2
            [
                ("L rotation (Q)", "rotate_left"),
                ("R rotation (E)", "rotate_right"),
                ("+ scale (+)", "scale_up"),
                ("- scale (-)", "scale_down"),
                ("Flip hor. (H)", "flip_horizontal"),
            ]
        ]
        
        right_column_configs = [
            # Row 1
            [
                ("Prev (P)", "prev"),
                ("Next (N)", "next"),
            ],
            # Row 2
            [
                ("Reset (R)", "restore"),
                ("Exit (Esc)", "exit"),
            ]
        ]
        
        # Calculate positions
        left_col_width = 4 * (self.button_width + self.padding) - self.padding
        right_col_width = 2 * (self.button_width + self.padding) - self.padding
        gap = 220  # Gap between columns
        total_width = left_col_width + gap + right_col_width
        
        # Center everything horizontally
        start_x = (self.window_width - total_width) / 2
        right_col_x = start_x + left_col_width + gap
        
        # Create left column buttons
        for row, row_configs in enumerate(left_column_configs):
            y = 70 if row == 0 else 20  # Row 1 at y=70, Row 2 at y=20
            for i, (text, action) in enumerate(row_configs):
                x = start_x + i * (self.button_width + self.padding)
                buttons.append(Button(x, y, self.button_width, self.button_height, text, action))
        
        # Create right column buttons
        for row, row_configs in enumerate(right_column_configs):
            y = 70 if row == 0 else 20  # Row 1 at y=70, Row 2 at y=20
            for i, (text, action) in enumerate(row_configs):
                x = right_col_x + i * (self.button_width + self.padding)
                buttons.append(Button(x, y, self.button_width, self.button_height, text, action))

        return buttons

    def draw(self):
        # Save the current matrices and attributes
        glPushMatrix()
        glPushAttrib(GL_ALL_ATTRIB_BITS)
        
        # Switch to 2D orthographic projection for UI
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self.window_width, 0, self.window_height, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        # Draw menu background
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glColor3f(0.1, 0.1, 0.1)  # Dark background
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(self.window_width, 0)
        glVertex2f(self.window_width, self.menu_height)
        glVertex2f(0, self.menu_height)
        glEnd()

        # Draw buttons with text
        for button in self.buttons:
            # Draw button background
            color = button.hover_color if button.is_hovered else button.color
            glColor3f(*color)
            glBegin(GL_QUADS)
            glVertex2f(button.x, button.y)
            glVertex2f(button.x + button.width, button.y)
            glVertex2f(button.x + button.width, button.y + button.height)
            glVertex2f(button.x, button.y + button.height)
            glEnd()

            # Render text using pygame
            text_surface = self.font.render(button.text, True, (0, 0, 0))
            text_data = pg.image.tostring(text_surface, 'RGBA', True)
            text_width, text_height = text_surface.get_size()

            # Position for centered text
            text_x = button.x + (button.width - text_width) / 2
            text_y = button.y + (button.height - text_height) / 2

            # Draw text
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glRasterPos2f(text_x, text_y)
            glDrawPixels(text_width, text_height, GL_RGBA, GL_UNSIGNED_BYTE, text_data)
            glDisable(GL_BLEND)

        # Restore the previous matrices and attributes
        glPopAttrib()
        glPopMatrix()

    def handle_mouse(self, mouse_pos):
        mx, my = mouse_pos
        my = self.window_height - my  # Convert from pygame coordinates to OpenGL coordinates
        
        for button in self.buttons:
            button.is_hovered = (button.x <= mx <= button.x + button.width and
                               button.y <= my <= button.y + button.height)
            
    def handle_click(self, mouse_pos, figure):
        mx, my = mouse_pos
        my = self.window_height - my  # Convert from pygame coordinates to OpenGL coordinates
        
        for button in self.buttons:
            if (button.x <= mx <= button.x + button.width and
                button.y <= my <= button.y + button.height):
                self.perform_action(button.action, figure)

    def perform_action(self, action, figure):
        actions = {
            "move_up": lambda: figure.translate(0, 0.1),
            "move_down": lambda: figure.translate(0, -0.1),
            "move_left": lambda: figure.translate(-0.1, 0),
            "move_right": lambda: figure.translate(0.1, 0),
            "rotate_left": lambda: figure.rotate(-5),
            "rotate_right": lambda: figure.rotate(5),
            "scale_up": lambda: figure.scale(1.1),
            "scale_down": lambda: figure.scale(0.9),
            "restore": lambda: figure.restore(),
            "exit": lambda: pg.event.post(pg.event.Event(pg.QUIT)),
            "next": lambda: self.app.next_figure(),
            "prev": lambda: self.app.prev_figure(),
            "flip_horizontal": lambda: figure.flip_horizontal(),
            "flip_vertical": lambda: figure.flip_vertical()
        }
        if action in actions:
            actions[action]()


if __name__ == "__main__":
    # Get vertices and colors from functions
    figures_data = [
        get_cat_vertices(scale_factor=0.3),
        get_swan_vertices(scale_factor=0.3),
        get_snail_vertices(scale_factor=0.3),
        get_bat_vertices(scale_factor=0.01),
        get_wolf_vertices(scale_factor=0.05)
    ]
    
    # Unpack vertices and colors into separate lists
    figures_vertices = [data[0] for data in figures_data]
    figures_colors = [data[1] for data in figures_data]
    
    app = App(title="Animals", width=None, height=None, fullscreen=True,
              figure_vertices=figures_vertices, figure_colors=figures_colors)
