$env:PYTHONPATH = 'C:\Users\lakei\Documents\ChatGPT\New project\streamlit_preview_runtime'
$pythonExe = 'C:\Users\lakei\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$appPath = 'C:\Users\lakei\Documents\ChatGPT\New project\portfolio-app-publish\streamlit_app.py'

& $pythonExe -m streamlit run $appPath `
    --global.developmentMode false `
    --server.port 8501 `
    --server.headless true `
    --browser.gatherUsageStats false
