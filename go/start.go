package main

import (
	"os"
	"os/exec"
	"syscall"
)

func main() {
	err := os.Chdir("tarkov-map-tracker")
	if err != nil {
		println(err.Error())
		return
	}

	// Execute the Python script
	cmd := exec.Command("python", "gui.py")
	cmd.SysProcAttr = &syscall.SysProcAttr{CreationFlags: 0x08000000} // Windows creation flag to hide the console window
	err = cmd.Start()
	if err != nil {
		println(err.Error())
		return
	}
}
