# PixelTrigger Pro Setup Script
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "   PixelTrigger Pro - Quick Setup" -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

try {
    Write-Host "[1/3] Creating virtual environment..." -ForegroundColor Green
    python -m venv .venv
    
    Write-Host "[2/3] Installing dependencies..." -ForegroundColor Green
    & ".venv\Scripts\pip.exe" install -r requirements.txt
    
    Write-Host "[3/3] Setup complete!" -ForegroundColor Green
    Write-Host ""
    Write-Host "=========================================" -ForegroundColor Cyan
    Write-Host "Setup completed successfully!" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "To run PixelTrigger Pro:" -ForegroundColor White
    Write-Host "- Double-click 'run_pixeltrigger.bat'" -ForegroundColor Gray
    Write-Host "- Or run: python main.py" -ForegroundColor Gray
    Write-Host "=========================================" -ForegroundColor Cyan
    Write-Host ""
}
catch {
    Write-Host "ERROR: Setup failed" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""
    Write-Host "Please ensure Python 3.7+ is installed and accessible from PATH" -ForegroundColor Yellow
}

Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
