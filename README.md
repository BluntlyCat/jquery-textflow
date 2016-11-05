# jquery-textflow

A jQuery plugin showing animated texts. Available as [pure jquery plugin] (#jquery) or as [django app] (#django).

# Table of contents
* [jQuery Only] (#jquery)
* [Django App] (#django)
    * [Django multilingual support] (#multilingual)
* [Settings] (#settings)
* [Methods] (#methods)
* [Dependencies] (#dependencies)
* [License] (#license)


# <a name="jquery"></a> jQuery Only

##Example using

Add a link to the css file in your `<head>`:
```html
<head>
  ...
  <link rel="stylesheet" type="text/css" href="path/to/textflow.min.css"/>
  ...
</head>
```

Then, before the closing ```<body>``` tag add:

```html
<head>
  ...
  <link rel="stylesheet" type="text/css" href="path/to/textflow.min.css"/>
  ...
</head>
<body>
  ...
  <script type="text/javascript" src="path/to/jquery.textflow.min.js"></script>
</body>
```

Now add the ```<div>``` tag within the ```<body>``` tag where you want to show the texts:

**NOTE:** The ```data-texts``` attribute is optional. You can pass there your texts as a simple comma separated string but it is also possible to pass an array of texts through the settings in your javascript code as shown soon. If you use the ```data-texts``` attribute, the texts in the settings were ignored!

```html
<head>
  ...
  <link rel="stylesheet" type="text/css" href="path/to/textflow.min.css"/>
  ...
</head>
<body>
  ...
  <div id="textflow" data-texts="your,texts,here"></div>
  ...
  <script type="text/javascript" src="path/to/jquery.textflow.min.js"></script>
</body>
```

In your javascript file then add the initializing code

```javascript
$(document).ready(function() {
  $(element).textFlow({
    texts: ['Your', 'Text', 'Here']
  });
});
```

The plugin is now ready and you should see your texts.


***


# <a name="django"></a> Django App

##Example using

Install textflow using pip.

```bash
pip install django-textflow
```
 
Then open the ```settings.py``` file, find the ```INSTALLED_APPS``` section and enable the app.

```python
INSTALLED_APPS = (
    ...
    'textflow'
)
```

Now we have to create the database model. 
Open a terminal and change to the root directory of your project and create the models
```bash
cd path/to/project-root
python manage.py makemigrations textflow
python manage.py migrate textflow
```

If the models where successfully created, you should see a new entry ```Textflow``` on the admin page where you can add FlowObjects. 
Create a few entries just to proof if the app works correctly later.

If the texts are created we need to pass them to the template. So open your ```views.py``` file and go to the view where you want your texts to appear. 

Import the ```FlowObject``` model and pass the texts to the view by simply call the ```serialize``` method.

```python
from django.shortcuts import render
from textflow.models import FlowObject
...
def your_view(request):
  ...
  return render(request, 'template.html', {
    'texts': FlowObject.serialize(),
    ...
  })
```

Then open your ```template.html``` file. 
At the top of the file add the two template tags for static files and the textflow tag.

```django
{% load staticfiles %}
{% load textflow %}
```

Add a link to the css file in your `<head>`:
```django
<head>
  ...
  <link rel="stylesheet" type="text/css" href="{% static 'stylesheets/textflow.min.css' %}"/>
  ...
</head>
```

Then, before the closing ```<body>``` tag add:

```django
<head>
  ...
  <link rel="stylesheet" type="text/css" href="{% static 'stylesheets/textflow.min.css' %}"/>
  ...
</head>
<body>
  ...
  <script type="text/javascript" src="{% static 'javascripts/jquery.textflow.min.js' %}"></script>
</body>
```

Now call the ```textflow``` tag within the ```<body>``` tag where you want to show the texts:

```django
<head>
  ...
  <link rel="stylesheet" type="text/css" href="{% static 'stylesheets/textflow.min.css' %}"/>
  ...
</head>
<body>
  ...
  {% textflow texts %}
  ...
  <script type="text/javascript" src="{% static 'javascripts/jquery.textflow.min.js' %}"></script>
</body>
```

In your javascript file then add the initializing code

**NOTE:** The texts are passed to the ```data-texts``` attribute directly by the template tag. Any texts defined in settings were ignored.

```javascript
$(document).ready(function() {
  $(element).textFlow();
});
```

You are done and you should see your texts now.


***


## <a name="multilingual"></a> Multilingual support

You can add multilingual texts by installing the [django-modeltranslation] (https://github.com/deschler/django-modeltranslation) app. This can be done even if you have already created texts.

Install django-modeltranslation:

```bash
pip install django-modeltranslation
```

Enable the app in ```settings.py```:

```python
INSTALLED_APPS = (
    ...
    'modeltranslation',
    'textflow',
)
```

Update your models:

```bash
cd path/to/project-root
python manage.py makemigrations textflow
python manage.py migrate textflow
```

Each FlowObject now should have a text field for each language. If you go to the admin page and open a FlowObject or if you create a new one, you can see that there is no text field anymore. They are all replaced by fields like ```text_de_de``` or ```text_en_gb```, depending on the languages you have enabled.

Please refer to the official Django documentation for more information about [translation] (https://docs.djangoproject.com/el/1.10/topics/i18n/translation/#).


***


# <a name="settings"></a> Settings

Option | Type | Default | Description
------ | ---- | ------- | -----------
width | string/int: Any valid css unit | 100% | Sets the width in relation of the parent node
height | string/int: Any valid css unit | 200px | Sets the height
top | string/int: Any valid css unit | 0 | Sets the top position within the parent node
left | string/int: Any valid css unit | 0 | Sets the left position within the parent node
maxTexts | int | 15 | Sets the maximum amount of texts that are simultaneously shown
marginTop | int | 25 | The space in pixel between the top border and the text
marginBottom | int | 0 | The space in pixel between the bottom border and the text
texts | array | ['Add', ... 'here'] | The texts that are shown, ignored when using ```data-texts``` attribute
color | string: Any valid css unit | #000 | The text color
background | string: Any valid css unit | transparent | The background color of the canvas (This is actually not needed because the background of the textflow div can be set in css. However it might happen that this could be useful for some reason so it is there... :)
font | string | sans-serif | The font family of the texts


***


# <a name="methods"></a> Methods

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


***


# <a name="dependencies"></a> Dependencies

jQuery 1.3

**For Django also**

Django 1.8

##For multilingual support (Django only)

django-modeltranslation

Refer to the official [documentation] (http://django-modeltranslation.readthedocs.io/en/latest/installation.html) which version is required for your Django and Python combination


***


# <a name="license"></a> License

Copyright (c) 2014 Michael Jünger

Licensed under the MIT license.
