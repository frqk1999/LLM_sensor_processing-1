@echo off
setlocal enabledelayedexpansion
set model="gpt-4o"
set modes=api
set n=5

set evals=self_coding

for %%m in (%modes%) do (
    for %%e in (%evals%) do (
        for %%f in (query/*.txt) do (
            set "file=%%f"
            set "filename=%%f"

            :: Remove directory prefix
            for %%i in ("!filename!") do set "filename=%%~ni%%~xi"

            :: Remove file extension
            for %%i in ("!filename!") do set "filename_without_ext=%%~ni"

            for /l %%i in (1,1,3) do (
                echo Running: python cli.py --query !filename_without_ext! --index %%i --mode %%m --openai !model! --write_to_csv --num_trial !n! --eval %%e
                python cli.py --query !filename_without_ext! --index %%i --mode %%m --openai !model! --write_to_csv --num_trial !n! --eval %%e
            )
        )
    )
)