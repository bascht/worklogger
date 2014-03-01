worklogger
==========
> Your friendly neighbourhood Worklog housekeeper. 


[![Build Status](https://travis-ci.org/bascht/worklogger.png?branch=master)](https://travis-ci.org/bascht/worklogger)



Worklogger helps keeping track of your daily work activities. It just sits in the background
and pops open now and then to ask you, what you've been doing for the last hour. To give you
some context, it will display the last two entries.

![Worklogger in action](https://raw.github.com/bascht/worklogger/master/screenshot.png)

The resulting file is a simple Markdown-file with a section for each day and a `@location`:

```markdown
# 01.03.2014 Saturday

## (16:27 - 20:00)
* @Tondorf
* 16:27 Research Python mocking frameworks
* 17:27 Took a nap
* 18:27 Fixed weird module-namespace @patch
* 19:27 Added documentation & screenshot
```

## Installation

You can install worklogger via pip:

    $ pip install worklogger

## Usage

To start a new day and the worklogger loop just call

    $ worklogger start
    
To display help and parameters:

    $ worklogger -h
