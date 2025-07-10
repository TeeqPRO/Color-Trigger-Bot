# PixelTrigger Pro v2.0

[![GitHub release](https://img.shields.io/github/v/release/TeeqPRO/PixelTrigger-PRO)](https://github.com/TeeqPRO/PixelTrigger-PRO/releases)
[![GitHub downloads](https://img.shields.io/github/downloads/TeeqPRO/PixelTrigger-PRO/total)](https://github.com/TeeqPRO/PixelTrigger-PRO/releases)
[![GitHub license](https://img.shields.io/github/license/TeeqPRO/PixelTrigger-PRO)](https://github.com/TeeqPRO/PixelTrigger-PRO/blob/main/LICENSE)

**Advanced Pixel Monitoring System**

A professional-grade application for monitoring pixel changes and automating mouse clicks with a modern, customizable interface.

## 📥 Download

**[📦 Download Latest Release](https://github.com/TeeqPRO/PixelTrigger-PRO/releases/latest)**

Choose from:
- **Standalone Executable** (.exe) - No Python installation required
- **Source Code** (.zip) - For Python developers and customization

## 🚀 Features

### Core Functionality
- **Real-time Pixel Monitoring**: Detects changes in pixels around your cursor position
- **Automatic Mouse Clicking**: Performs clicks when pixel changes are detected
- **Customizable Sensitivity**: 5-level sensitivity adjustment for different use cases
- **Multiple Click Types**: Left click, right click, and double click options

### User Interface
- **Modern Professional Design**: Clean, intuitive interface with dark/light themes
- **Always on Top Option**: Keep the window visible above other applications
- **Status Indicators**: Real-time monitoring status with color-coded feedback
- **Compact Design**: Space-efficient layout that doesn't clutter your desktop

### Customization Options
- **Hotkey Binding**: Customizable function key shortcuts (F1-F12)
- **Offset Distance**: Adjustable pixel monitoring distance
- **Detection Delay**: Configurable check intervals for performance optimization
- **Auto-stop Mode**: Option to automatically stop after first detection

### Additional Features
- **🔄 Restart Function**: Built-in restart button to refresh the application
- **📁 Settings Persistence**: Automatic saving and loading of all configurations
- **🎨 Theme Support**: Switch between professional dark and light themes
- **🔧 Advanced Configuration**: Fine-tune every aspect of pixel detection

## � Project Structure

```
PixelTrigger-Pro/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # This documentation
├── LICENSE                # MIT license
├── CONTRIBUTING.md        # Contribution guidelines
├── version.json           # Version information
├── .gitignore            # Git ignore rules
├── setup.bat             # Windows setup script
├── setup.ps1             # PowerShell setup script
├── run_pixeltrigger.bat  # Launch script
└── .venv/                # Virtual environment (created after setup)
```

## �📋 Requirements

- Python 3.7+
- Windows OS (for keyboard hotkey support)
- Required packages (automatically installed):
  - `pyautogui` - Screen automation
  - `keyboard` - Global hotkey detection
  - `Pillow` - Image processing for icon

## 🛠️ Installation

### Quick Start
1. **Download** the latest release from [GitHub Releases](https://github.com/TeeqPRO/PixelTrigger-PRO/releases)
2. **Extract** the files to your desired location
3. **Setup** (first time only):
   - Run `setup.bat` (Windows) or `setup.ps1` (PowerShell) to install dependencies
4. **Launch** the application:
   - Double-click `run_pixeltrigger.bat`
   - Or run `python main.py` from the command line

### From Source
1. **Clone** the repository:
   ```bash
   git clone https://github.com/TeeqPRO/PixelTrigger-PRO.git
   cd PixelTrigger-PRO
   ```
2. **Setup** the environment:
   ```bash
   # Windows
   setup.bat
   
   # Or manually
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Run** the application:
   ```bash
   python main.py
   ```

## 🎯 How to Use

### Basic Operation
1. **Launch** the application
2. **Position** your cursor where you want to monitor
3. **Start monitoring** by:
   - Clicking the "▶ Start Monitor" button, or
   - Pressing your assigned hotkey (default: F6)
4. **Monitor status** will show "MONITORING" in green
5. **Automatic clicking** occurs when pixel changes are detected

### Hotkeys
- **Start Monitor**: F6 (customizable in settings)
- **Stop Monitor**: ESC key

### Settings Configuration

#### Quick Settings (Main Window)
- **Start Hotkey**: Choose from F1-F12 function keys
- **Sensitivity**: Adjust from 1 (least sensitive) to 5 (most sensitive)
- **Always on Top**: Keep window above other applications
- **Auto-stop**: Stop monitoring after first detection

#### Advanced Settings (Settings Window)
- **Theme**: Switch between dark and light interface themes
- **Click Type**: Choose left click, right click, or double click
- **Pixel Offset Distance**: Set monitoring distance from cursor (1-10 pixels)
- **Check Delay**: Adjust monitoring frequency (1-100ms)

## 🔧 Configuration

### Settings File
All settings are automatically saved to `settings.json` in the application directory. This file includes:
- Hotkey bindings
- Sensitivity levels
- UI preferences
- Monitoring parameters

### Default Settings
```json
{
    "hotkey": "f6",
    "stop_key": "esc",
    "click_delay": 0.01,
    "offset_distance": 2,
    "theme": "dark",
    "always_on_top": true,
    "auto_stop": true,
    "click_type": "left",
    "sensitivity": 1
}
```

## 💡 Tips for Optimal Use

### Sensitivity Settings
- **Level 1**: Only detects major color changes (least false positives)
- **Level 3**: Balanced sensitivity for general use
- **Level 5**: Detects subtle changes (most responsive)

### Performance Optimization
- Lower check delay for faster response (higher CPU usage)
- Higher check delay for lower CPU usage (slightly slower response)
- Adjust offset distance based on your monitoring needs

### Use Cases
- **Gaming**: Auto-click when specific UI elements change
- **Automation**: Trigger actions when screen content updates
- **Monitoring**: React to visual changes in applications
- **Accessibility**: Assist with repetitive clicking tasks

## 🖥️ Screenshots

![Main Interface](https://github.com/TeeqPRO/PixelTrigger-PRO/blob/main/screenshots/main-interface.png)
*Main interface with dark theme*

![Settings Panel](https://github.com/TeeqPRO/PixelTrigger-PRO/blob/main/screenshots/settings-panel.png)
*Advanced settings configuration*

## 🎨 Interface Overview

### Main Window Components
- **Status Display**: Shows current monitoring state with color indicators
- **Control Buttons**: Start/Stop monitoring with clear visual feedback
- **Quick Settings**: Immediate access to common configuration options
- **Advanced Options**: Checkboxes for additional features
- **Action Buttons**: Access to settings, help, about information, and restart functionality

### Status Indicators
- **🔴 IDLE**: Not monitoring (red)
- **🟢 MONITORING**: Actively watching for changes (green)
- **🟡 DETECTED**: Change detected, clicking in progress (yellow)

## 🔒 Privacy & Security

- **No Network Access**: Application runs entirely offline
- **Local Settings**: All configuration stored locally in JSON format
- **No Data Collection**: No user data or usage statistics collected
- **Open Source**: Full source code available for review

## 🆘 Troubleshooting

### Common Issues

**Application won't start**
- Ensure Python 3.7+ is installed
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Run from command line to see error messages

**Hotkeys not working**
- Run application as administrator (required for global hotkeys)
- Check that the hotkey isn't used by another application
- Try a different function key in settings

**Detection not working**
- Adjust sensitivity level (try level 3 or higher)
- Check offset distance setting
- Ensure cursor is positioned over changing pixels

**High CPU usage**
- Increase check delay in advanced settings
- Lower sensitivity if not needed
- Close other resource-intensive applications

### Error Messages
If you encounter errors, check:
1. Python version compatibility
2. Required package installation
3. Administrator privileges for hotkey functionality
4. Available system resources

## 📝 Version History

### v2.0 (Current)
- Complete UI redesign with professional appearance
- Added theme support (dark/light modes)
- Implemented settings persistence
- Enhanced customization options
- Added sensitivity levels
- Improved error handling
- Added comprehensive help system

### v1.0 (Previous)
- Basic pixel monitoring functionality
- Simple GUI interface
- F6 hotkey support
- Basic click detection

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](https://github.com/TeeqPRO/PixelTrigger-PRO/blob/main/CONTRIBUTING.md) for details.

### How to Contribute
1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

## 🆘 Support & Issues

### Getting Help
- **📖 Documentation**: Check this README and in-app help (❓ Help button)
- **🐛 Bug Reports**: [Create an issue](https://github.com/TeeqPRO/PixelTrigger-PRO/issues/new?template=bug_report.md)
- **💡 Feature Requests**: [Request a feature](https://github.com/TeeqPRO/PixelTrigger-PRO/issues/new?template=feature_request.md)
- **💬 Discussions**: [Join the discussion](https://github.com/TeeqPRO/PixelTrigger-PRO/discussions)

### Quick Links
- **🏠 Repository**: [https://github.com/TeeqPRO/PixelTrigger-PRO](https://github.com/TeeqPRO/PixelTrigger-PRO)
- **📦 Releases**: [https://github.com/TeeqPRO/PixelTrigger-PRO/releases](https://github.com/TeeqPRO/PixelTrigger-PRO/releases)
- **📋 Issues**: [https://github.com/TeeqPRO/PixelTrigger-PRO/issues](https://github.com/TeeqPRO/PixelTrigger-PRO/issues)
- **📊 Project Board**: [https://github.com/TeeqPRO/PixelTrigger-PRO/projects](https://github.com/TeeqPRO/PixelTrigger-PRO/projects)

## 📄 License

This project is provided as-is for educational and personal use.

---

**PixelTrigger Pro** - Professional Pixel Monitoring System  
© 2025 - Advanced automation made simple

**Star ⭐ this repository if you find it useful!**

Made with ❤️ by [TeeqPRO](https://github.com/TeeqPRO)
