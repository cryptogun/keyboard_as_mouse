# Keyboard as Mouse
Use shortcut keys to coutrol cursor.  
Opensource, if you worry about keyboard tracking virus too.  
But I don't have time to audit(full review) the [`keyboard`](https://pypi.python.org/pypi/keyboard) module.  

## Dependence
[`keyboard`](https://pypi.python.org/pypi/keyboard) module

## Usage
```cmd
pip install keyboard
```
Change shortcut keys for your preference in `keyboard_as_mouse.py`.  

## Function examples  
```text
Left  click            :        ctrl+space  
Right click            :        alt+space  
Double left click      :        ctrl+space+space  
Text selection begin   :        ctrl+shift+u  
Text selection ended   :        ctrl+shift+o  
Cursor fast move       :        alt+j/l/i/k  
Cursor slow move       :        ctrl+shift+j/l/i/k  
Drag and drop          :        same as text selection.  
Full screen positioning:  
                           ctrl+7890  
                                jkl;  
                                m,./  
Exit program           :        esc,esc,esc  
```
