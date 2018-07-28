# Pycharm 学习
[网址](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)


## Step 4. Code with smart assistance

- code completion
- Intention action (Click the lightbulb (or press Alt+Enter) )

## Step 5. Keep your code neat

> Every time the IDE finds unused code, an endless loop, and many other things that likely require your attention, you’ll see a lightbulb. Click it, or press Alt+Enter, to apply a fix.

> he complete list of available inspections can be found under Settings | Editor | Inspections (or PyCharm | Preferences | Editor | Inspections for macOS users). Disable some of them, or enable others, plus adjust the severity of each inspection. You decide whether it should be considered an error or just a warning.

## Step 7. Find your way through

### Basic search
> With these search facilities, you can find and replace any fragment of code both in the currently opened file (Ctrl+F), or in an entire project (Ctrl+Shift+F).

### Search for usages

>To find where a particular symbol is used, PyCharm suggests full-scale search via Find Usages (Alt+F7):


### Project navigation
> You can tell a lot just looking at your File Structure, with its imports or call hierarchies:

Also, you can navigate to:

> Class by its name (Ctrl+N).
> File by its name (Ctrl+Shift+N):
> Symbol by its name (Ctrl+Shift+Alt+N).
> Symbol by its name (Ctrl+Shift+Alt+N).
> Declaration (Ctrl+B).
> Base class/base function (Ctrl+U). 

### Find Action
Take advantage of many smart actions possible with PyCharm. For example, use the Find Action search (Ctrl+Shift+A): just type a part of the action name, and the IDE will show you the list of all available options. Then, select the action you need:

### Search Everywhere
If you have a general idea of what you're looking for, you can always locate the corresponding element using one of the existing navigation features. But what if you really want to look for something in every nook and cranny? The answer is to use Search Everywhere!


## Step 8. Run, debug and test

## Step 9. Keep your source code under Version Control

## Step 10. Remote development


## 常用

### Scientific mode
[网址](https://www.jetbrains.com/help/pycharm/matplotlib-support.html)

有啥用？
> Scientific mode in PyCharm provides support for interactive scientific computing and data visualization. The following packages must be properly installed: Matplotlib and Numpy

具体
1 (document 显示)The Documentation tool window appears (a pinned version of the quick documentation lookup), showing the inline documentation for the symbol at caret:

2  (special variable) DataFrame/Array view appears in the Python console and in the Debug tool window.

3 In the Scientific mode, a graph opens in its own tab in the SciView window, allowing you to resize it, zoom in and out, etc. You can alter this behavior by toggling the Show plots in tool window check box (Settings/Preferences | Tools | Python Scientific).

4 When you open SciView tool window with the debug session stopped, an empty tab is shown, where you can type the variables from the console:

5  Pycharm3 新增了（科学模式）Scientific mode。在普通的项目里如果不需要使用到Scientific mode，可以选择关闭它。
- View > 去掉Scientific Mode的勾选
- Settings > Tools > Python Scientific > Show plots in tool window 关闭

