import cx_Freeze


executables = [cx_Freeze.Executable("janela.py")]

cx_Freeze.setup(
    name="Bot pra instagram",
    options={"build_exe": {"packages":["PySide2","pyautogui"],
                           "include_file":["cfollowing.PNG","follow.PNG","followers.PNG","following.PNG","parar.PNG","profile.PNG","search.PNG","unfollow.PNG","x.PNG"]}},
    executables = executables                      

)


