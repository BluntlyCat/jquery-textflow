# jquery-textflow

[1]: <https://github.com/kenwheeler/slick>

A JQuery plugin showing animated texts

#####Example using

Add a link to the css file in your `<head>`:
```html
<link rel="stylesheet" type="text/css" href="path/to/textflow.min.css"/>
```

Then, before the closing ```<body>``` tag add:

```html
<script type="text/javascript" src="path/to/jquery.textflow.min.js"></script>
```

### Settings

Option | Type | Default | Description
------ | ---- | ------- | -----------
width | string/int: Any valid css unit | 100% | Sets the width in relation of the parent node
height | string/int: Any valid css unit | 200px | Sets the height
top | string/int: Any valid css unit | 0 | Sets the top position within the parent node
left | string/int: Any valid css unit | 0 | Sets the left position within the parent node
maxTexts | int | 15 | Sets the maximum amount of texts that are simultaneously shown
marginTop | int | 25 | The space in pixel between the top border and the text
marginBottom | int | 0 | The space in pixel between the bottom border and the text
texts | array | ['Add', ... 'here'] | The texts that are shown
color | string: Any valid css unit | #000 | The text color
background | string: Any valid css unit | transparent | The background color of the canvas (This is actually not needed because the background of the textflow div can be set in css. However it might happen that this could be useful for some reason so it is there... :)
font | string | sans-serif | The font family of the texts

#### Methods

Methods are called on textflow instances:

```javascript

// Get the instance
var textflow = $('.your-element').textFlow({options...});

// Stop textflow
textflow.stopTextFlow();

// Start textflow
textflow.startTextFlow();
```


Method | Argument | Description
------ | -------- | -----------
`startTextFlow` | options : None | Start textflow if not active
`stopTextFlow` | options : None | Stop textflow if active


#### Example

Initialize with:

```javascript
$(element).textFlow({
  texts: ['Your', 'Text', 'Here']
});
```


#### Dependencies
 
jQuery 1.3


#### License

Copyright (c) 2014 Michael Jünger

Licensed under the MIT license.
