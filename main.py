import pyautogui
import keyboard
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
import json
import os
from PIL import Image, ImageTk
import io
import base64

class PixelTriggerPro:
    def __init__(self):
        self.monitoring = False
        self.window = None
        self.settings = self.load_settings()
        self.setup_gui()
        
    def load_settings(self):
        """Load settings from JSON file or create default settings"""
        default_settings = {
            "hotkey": "f6",
            "stop_key": "esc",
            "click_delay": 0.01,
            "offset_distance": 2,
            "theme": "dark",
            "always_on_top": True,
            "auto_stop": True,
            "click_type": "left",
            "sensitivity": 1
        }
        
        try:
            if os.path.exists("settings.json"):
                with open("settings.json", "r") as f:
                    settings = json.load(f)
                    # Merge with defaults for any missing keys
                    for key, value in default_settings.items():
                        if key not in settings:
                            settings[key] = value
                    return settings
        except:
            pass
        return default_settings
    
    def save_settings(self):
        """Save current settings to JSON file"""
        try:
            with open("settings.json", "w") as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {str(e)}")
    
    def create_icon(self):
        """Create a simple icon for the application"""
        # Create a simple icon using PIL
        img = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
        pixels = img.load()
        
        # Draw a simple eye-like icon
        for i in range(32):
            for j in range(32):
                x, y = i - 16, j - 16
                if x*x + y*y < 144:  # Outer circle
                    pixels[i, j] = (52, 152, 219, 255)  # Blue
                if x*x + y*y < 64:   # Inner circle
                    pixels[i, j] = (44, 62, 80, 255)   # Dark blue
                if x*x + y*y < 16:   # Pupil
                    pixels[i, j] = (231, 76, 60, 255)  # Red
        
        return ImageTk.PhotoImage(img)
    
    def setup_gui(self):
        """Create the main GUI window"""
        self.window = tk.Tk()
        self.window.title("PixelTrigger Pro v2.0")
        self.window.geometry("420x580")
        self.window.resizable(False, False)
        
        # Set icon
        try:
            icon = self.create_icon()
            self.window.iconphoto(True, icon)
        except:
            pass
        
        # Configure style
        self.apply_theme()
        
        # Set always on top if enabled
        if self.settings["always_on_top"]:
            self.window.wm_attributes("-topmost", True)
        
        self.create_widgets()
        self.start_keyboard_listener()
    
    def apply_theme(self):
        """Apply the selected theme"""
        if self.settings["theme"] == "dark":
            bg_color = "#2c3e50"
            fg_color = "#ecf0f1"
            accent_color = "#3498db"
            button_bg = "#34495e"
        else:
            bg_color = "#ecf0f1"
            fg_color = "#2c3e50"
            accent_color = "#3498db"
            button_bg = "#bdc3c7"
        
        self.window.configure(bg=bg_color)
        self.colors = {
            "bg": bg_color,
            "fg": fg_color,
            "accent": accent_color,
            "button_bg": button_bg
        }
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Title Frame
        title_frame = tk.Frame(self.window, bg=self.colors["bg"])
        title_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title_label = tk.Label(title_frame, text="PixelTrigger Pro", 
                              font=("Segoe UI", 18, "bold"), 
                              fg=self.colors["accent"], bg=self.colors["bg"])
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Advanced Pixel Monitoring System", 
                                 font=("Segoe UI", 9), 
                                 fg=self.colors["fg"], bg=self.colors["bg"])
        subtitle_label.pack()
        
        # Status Frame
        status_frame = tk.LabelFrame(self.window, text="Status", 
                                    font=("Segoe UI", 10, "bold"),
                                    fg=self.colors["fg"], bg=self.colors["bg"])
        status_frame.pack(fill="x", padx=20, pady=10)
        
        self.status_label = tk.Label(status_frame, text="● IDLE", 
                                    font=("Segoe UI", 12, "bold"), 
                                    fg="#e74c3c", bg=self.colors["bg"])
        self.status_label.pack(pady=10)
        
        # Control Buttons Frame
        control_frame = tk.LabelFrame(self.window, text="Controls", 
                                     font=("Segoe UI", 10, "bold"),
                                     fg=self.colors["fg"], bg=self.colors["bg"])
        control_frame.pack(fill="x", padx=20, pady=10)
        
        button_frame = tk.Frame(control_frame, bg=self.colors["bg"])
        button_frame.pack(pady=10)
        
        self.start_btn = tk.Button(button_frame, text="▶ Start Monitor", 
                                  command=self.start_monitoring,
                                  font=("Segoe UI", 10, "bold"),
                                  bg="#27ae60", fg="white",
                                  width=12, height=2,
                                  relief="flat", bd=0)
        self.start_btn.pack(side="left", padx=5)
        
        self.stop_btn = tk.Button(button_frame, text="⏹ Stop Monitor", 
                                 command=self.stop_monitoring,
                                 font=("Segoe UI", 10, "bold"),
                                 bg="#e74c3c", fg="white",
                                 width=12, height=2,
                                 relief="flat", bd=0,
                                 state="disabled")
        self.stop_btn.pack(side="left", padx=5)
        
        # Quick Settings Frame
        quick_frame = tk.LabelFrame(self.window, text="Quick Settings", 
                                   font=("Segoe UI", 10, "bold"),
                                   fg=self.colors["fg"], bg=self.colors["bg"])
        quick_frame.pack(fill="x", padx=20, pady=10)
        
        # Hotkey setting
        hotkey_frame = tk.Frame(quick_frame, bg=self.colors["bg"])
        hotkey_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(hotkey_frame, text="Start Hotkey:", 
                font=("Segoe UI", 9), fg=self.colors["fg"], bg=self.colors["bg"]).pack(side="left")
        
        self.hotkey_var = tk.StringVar(value=self.settings["hotkey"].upper())
        hotkey_combo = ttk.Combobox(hotkey_frame, textvariable=self.hotkey_var, 
                                   values=["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"],
                                   width=8, state="readonly")
        hotkey_combo.pack(side="right")
        hotkey_combo.bind("<<ComboboxSelected>>", self.update_hotkey)
        
        # Sensitivity setting
        sens_frame = tk.Frame(quick_frame, bg=self.colors["bg"])
        sens_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(sens_frame, text="Sensitivity:", 
                font=("Segoe UI", 9), fg=self.colors["fg"], bg=self.colors["bg"]).pack(side="left")
        
        self.sensitivity_var = tk.IntVar(value=self.settings["sensitivity"])
        sens_scale = tk.Scale(sens_frame, from_=1, to=5, orient="horizontal",
                             variable=self.sensitivity_var, command=self.update_sensitivity,
                             bg=self.colors["bg"], fg=self.colors["fg"],
                             highlightthickness=0, length=100)
        sens_scale.pack(side="right")
        
        # Advanced Settings Frame
        advanced_frame = tk.LabelFrame(self.window, text="Advanced Options", 
                                      font=("Segoe UI", 10, "bold"),
                                      fg=self.colors["fg"], bg=self.colors["bg"])
        advanced_frame.pack(fill="x", padx=20, pady=10)
        
        # Checkboxes
        self.always_top_var = tk.BooleanVar(value=self.settings["always_on_top"])
        always_top_cb = tk.Checkbutton(advanced_frame, text="Always on top", 
                                      variable=self.always_top_var,
                                      command=self.toggle_always_on_top,
                                      font=("Segoe UI", 9),
                                      fg=self.colors["fg"], bg=self.colors["bg"],
                                      selectcolor=self.colors["button_bg"])
        always_top_cb.pack(anchor="w", padx=10, pady=2)
        
        self.auto_stop_var = tk.BooleanVar(value=self.settings["auto_stop"])
        auto_stop_cb = tk.Checkbutton(advanced_frame, text="Auto-stop after detection", 
                                     variable=self.auto_stop_var,
                                     command=self.update_auto_stop,
                                     font=("Segoe UI", 9),
                                     fg=self.colors["fg"], bg=self.colors["bg"],
                                     selectcolor=self.colors["button_bg"])
        auto_stop_cb.pack(anchor="w", padx=10, pady=2)
        
        # Action Buttons Frame
        action_frame = tk.Frame(self.window, bg=self.colors["bg"])
        action_frame.pack(fill="x", padx=20, pady=20)
        
        settings_btn = tk.Button(action_frame, text="⚙ Settings", 
                                command=self.open_settings,
                                font=("Segoe UI", 9),
                                bg=self.colors["button_bg"], fg=self.colors["fg"],
                                width=10, height=1, relief="flat", bd=1)
        settings_btn.pack(side="left", padx=5)
        
        help_btn = tk.Button(action_frame, text="❓ Help", 
                            command=self.show_help,
                            font=("Segoe UI", 9),
                            bg=self.colors["button_bg"], fg=self.colors["fg"],
                            width=10, height=1, relief="flat", bd=1)
        help_btn.pack(side="left", padx=5)
        
        about_btn = tk.Button(action_frame, text="ℹ About", 
                             command=self.show_about,
                             font=("Segoe UI", 9),
                             bg=self.colors["button_bg"], fg=self.colors["fg"],
                             width=10, height=1, relief="flat", bd=1)
        about_btn.pack(side="right", padx=5)
        
        restart_btn = tk.Button(action_frame, text="🔄 Restart", 
                               command=self.restart_app,
                               font=("Segoe UI", 9),
                               bg=self.colors["button_bg"], fg=self.colors["fg"],
                               width=10, height=1, relief="flat", bd=1)
        restart_btn.pack(side="right", padx=5)
    
    def update_status(self, status, color):
        """Update the status label"""
        self.status_label.config(text=f"● {status}", fg=color)
    
    def get_offset_colors(self):
        """Get pixel colors at offset positions from cursor"""
        x, y = pyautogui.position()
        offset = self.settings["offset_distance"]
        left_pixel = pyautogui.pixel(x - offset, y)
        right_pixel = pyautogui.pixel(x + offset, y)
        return left_pixel, right_pixel
    
    def monitor_pixels(self):
        """Main monitoring function"""
        self.update_status("MONITORING", "#27ae60")
        initial_left, initial_right = self.get_offset_colors()
        time.sleep(0.1)
        
        while self.monitoring:
            if keyboard.is_pressed(self.settings["stop_key"]):
                self.stop_monitoring()
                break
            
            left, right = self.get_offset_colors()
            
            # Check for changes based on sensitivity
            left_diff = sum(abs(a - b) for a, b in zip(left, initial_left))
            right_diff = sum(abs(a - b) for a, b in zip(right, initial_right))
            
            threshold = 50 / self.settings["sensitivity"]  # Higher sensitivity = lower threshold
            
            if left_diff > threshold or right_diff > threshold:
                self.update_status("DETECTED - CLICKING", "#f39c12")
                
                if self.settings["click_type"] == "left":
                    pyautogui.click()
                elif self.settings["click_type"] == "right":
                    pyautogui.rightClick()
                elif self.settings["click_type"] == "double":
                    pyautogui.doubleClick()
                
                if self.settings["auto_stop"]:
                    self.stop_monitoring()
                break
            
            time.sleep(self.settings["click_delay"])
    
    def start_monitoring(self):
        """Start pixel monitoring"""
        if not self.monitoring:
            self.monitoring = True
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            threading.Thread(target=self.monitor_pixels, daemon=True).start()
    
    def stop_monitoring(self):
        """Stop pixel monitoring"""
        self.monitoring = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.update_status("IDLE", "#e74c3c")
    
    def keyboard_listener(self):
        """Listen for hotkey presses"""
        while True:
            try:
                if keyboard.is_pressed(self.settings["hotkey"]):
                    if not self.monitoring:
                        self.start_monitoring()
                    time.sleep(0.3)  # Prevent multiple triggers
            except:
                pass
            time.sleep(0.1)
    
    def start_keyboard_listener(self):
        """Start the keyboard listener thread"""
        threading.Thread(target=self.keyboard_listener, daemon=True).start()
    
    def update_hotkey(self, event=None):
        """Update hotkey setting"""
        self.settings["hotkey"] = self.hotkey_var.get().lower()
        self.save_settings()
    
    def update_sensitivity(self, value):
        """Update sensitivity setting"""
        self.settings["sensitivity"] = int(value)
        self.save_settings()
    
    def toggle_always_on_top(self):
        """Toggle always on top setting"""
        self.settings["always_on_top"] = self.always_top_var.get()
        self.window.wm_attributes("-topmost", self.settings["always_on_top"])
        self.save_settings()
    
    def update_auto_stop(self):
        """Update auto stop setting"""
        self.settings["auto_stop"] = self.auto_stop_var.get()
        self.save_settings()
    
    def open_settings(self):
        """Open advanced settings window"""
        settings_window = tk.Toplevel(self.window)
        settings_window.title("Advanced Settings")
        settings_window.geometry("400x500")
        settings_window.resizable(False, False)
        settings_window.configure(bg=self.colors["bg"])
        
        if self.settings["always_on_top"]:
            settings_window.wm_attributes("-topmost", True)
        
        # Settings content
        main_frame = tk.Frame(settings_window, bg=self.colors["bg"])
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Theme selection
        theme_frame = tk.LabelFrame(main_frame, text="Theme", font=("Segoe UI", 10, "bold"),
                                   fg=self.colors["fg"], bg=self.colors["bg"])
        theme_frame.pack(fill="x", pady=10)
        
        theme_var = tk.StringVar(value=self.settings["theme"])
        
        tk.Radiobutton(theme_frame, text="Dark Theme", variable=theme_var, value="dark",
                      font=("Segoe UI", 9), fg=self.colors["fg"], bg=self.colors["bg"],
                      selectcolor=self.colors["button_bg"]).pack(anchor="w", padx=10, pady=2)
        
        tk.Radiobutton(theme_frame, text="Light Theme", variable=theme_var, value="light",
                      font=("Segoe UI", 9), fg=self.colors["fg"], bg=self.colors["bg"],
                      selectcolor=self.colors["button_bg"]).pack(anchor="w", padx=10, pady=2)
        
        # Click type
        click_frame = tk.LabelFrame(main_frame, text="Click Type", font=("Segoe UI", 10, "bold"),
                                   fg=self.colors["fg"], bg=self.colors["bg"])
        click_frame.pack(fill="x", pady=10)
        
        click_var = tk.StringVar(value=self.settings["click_type"])
        
        for click_type, label in [("left", "Left Click"), ("right", "Right Click"), ("double", "Double Click")]:
            tk.Radiobutton(click_frame, text=label, variable=click_var, value=click_type,
                          font=("Segoe UI", 9), fg=self.colors["fg"], bg=self.colors["bg"],
                          selectcolor=self.colors["button_bg"]).pack(anchor="w", padx=10, pady=2)
        
        # Advanced options
        advanced_frame = tk.LabelFrame(main_frame, text="Advanced", font=("Segoe UI", 10, "bold"),
                                      fg=self.colors["fg"], bg=self.colors["bg"])
        advanced_frame.pack(fill="x", pady=10)
        
        # Offset distance
        offset_frame = tk.Frame(advanced_frame, bg=self.colors["bg"])
        offset_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(offset_frame, text="Pixel Offset Distance:", 
                font=("Segoe UI", 9), fg=self.colors["fg"], bg=self.colors["bg"]).pack(side="left")
        
        offset_var = tk.IntVar(value=self.settings["offset_distance"])
        offset_spin = tk.Spinbox(offset_frame, from_=1, to=10, textvariable=offset_var,
                                width=5, font=("Segoe UI", 9))
        offset_spin.pack(side="right")
        
        # Click delay
        delay_frame = tk.Frame(advanced_frame, bg=self.colors["bg"])
        delay_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(delay_frame, text="Check Delay (ms):", 
                font=("Segoe UI", 9), fg=self.colors["fg"], bg=self.colors["bg"]).pack(side="left")
        
        delay_var = tk.DoubleVar(value=self.settings["click_delay"] * 1000)
        delay_spin = tk.Spinbox(delay_frame, from_=1, to=100, textvariable=delay_var,
                               width=8, font=("Segoe UI", 9))
        delay_spin.pack(side="right")
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg=self.colors["bg"])
        button_frame.pack(fill="x", pady=20)
        
        def save_advanced_settings():
            self.settings["theme"] = theme_var.get()
            self.settings["click_type"] = click_var.get()
            self.settings["offset_distance"] = offset_var.get()
            self.settings["click_delay"] = delay_var.get() / 1000
            self.save_settings()
            settings_window.destroy()
            messagebox.showinfo("Settings", "Settings saved! Restart the application to apply theme changes.")
        
        tk.Button(button_frame, text="Save Settings", command=save_advanced_settings,
                 font=("Segoe UI", 10, "bold"), bg="#27ae60", fg="white",
                 relief="flat", bd=0).pack(side="right", padx=5)
        
        tk.Button(button_frame, text="Cancel", command=settings_window.destroy,
                 font=("Segoe UI", 10), bg=self.colors["button_bg"], fg=self.colors["fg"],
                 relief="flat", bd=0).pack(side="right", padx=5)
    
    def show_help(self):
        """Show help dialog"""
        help_text = """PixelTrigger Pro - Help

HOW TO USE:
1. Position your cursor where you want to monitor
2. Press the Start button or use the hotkey (default: F6)
3. The app will monitor pixels around your cursor
4. When a change is detected, it will click automatically

HOTKEYS:
• Start Monitor: F6 (customizable)
• Stop Monitor: ESC

FEATURES:
• Adjustable sensitivity (1-5)
• Multiple click types (left, right, double)
• Always on top option
• Auto-stop after detection
• Custom hotkey bindings
• Dark/Light themes

TIPS:
• Higher sensitivity = more responsive to small changes
• Lower sensitivity = only detects major changes
• Use offset distance to monitor specific areas
• Auto-stop prevents continuous clicking

GITHUB: https://github.com/TeeqPRO/PixelTrigger-PRO"""
        
        messagebox.showinfo("Help", help_text)
    
    def show_about(self):
        """Show about dialog"""
        about_text = """PixelTrigger Pro v2.0

Advanced Pixel Monitoring System

Created with Python & Tkinter
© 2025 PixelTrigger Pro

Features:
✓ Real-time pixel monitoring
✓ Customizable hotkeys
✓ Multiple click types
✓ Sensitivity adjustment
✓ Professional UI
✓ Settings persistence

GitHub: https://github.com/TeeqPRO/PixelTrigger-PRO
Releases: https://github.com/TeeqPRO/PixelTrigger-PRO/releases

For support and updates, visit our GitHub repository."""
        
        messagebox.showinfo("About PixelTrigger Pro", about_text)
    
    def restart_app(self):
        """Restart the application"""
        result = messagebox.askyesno("Restart Application", 
                                   "Are you sure you want to restart PixelTrigger Pro?\n\nThis will close the current window and start a new instance.")
        if result:
            self.monitoring = False
            self.save_settings()
            
            # Import required modules for restart
            import sys
            import subprocess
            
            # Start new instance
            subprocess.Popen([sys.executable] + sys.argv)
            
            # Close current instance
            self.window.destroy()
    
    def run(self):
        """Start the application"""
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()
    
    def on_closing(self):
        """Handle application closing"""
        self.monitoring = False
        self.save_settings()
        self.window.destroy()

if __name__ == "__main__":
    app = PixelTriggerPro()
    app.run()
