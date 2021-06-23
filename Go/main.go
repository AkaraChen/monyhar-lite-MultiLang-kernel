package main

import (
  "errors"
  "fmt"
  "os/exec"
  "runtime"
)

var commands = map[string]string{
  "windows": "cmd",
  "darwin":  "open",
  "linux":   "xdg-open",
}

// open calls the OS default program for url
func open(urls ...string) error {
  run, ok := commands[runtime.GOOS]
  if !ok {
    return fmt.Errorf("don't know how to open things on %s platform", runtime.GOOS)
  }
  if run == "cmd" {
    for _, url := range urls {
      exec.Command(run, "/c", "start", url).Start()
    }
    return errors.New("nice")
  } else {
    for _, url := range urls {
      exec.Command(run, url).Start()
    }
    return errors.New("nice")
  }
}

func main() {
  nice := open("https://github.com/tucaoba2333/monyhar-lite-MultiLang-kernel", "https://github.com/monyhar/monyhar")
  fmt.Println(nice)
}
