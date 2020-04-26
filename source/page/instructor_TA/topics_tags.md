# List of Topics and Tags 

## Topics

Reference: ([link](https://prairielearn.readthedocs.io/en/latest/course/#topics))

Each question in the course has a topic from the list specified in the `infoCourse.jsonfile`. Topics should be thought of as **chapters** or **sections** in a textbook, and there should be about 10 to 30 topics in a typical course. The topic properties are as follows.

| Property      | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| `name`        | Brief name for the topic. Shorter is better. Should be in sentence case (leading captial letter). |
| `color`       | The color scheme for this topic (see below for choices).     |
| `description` | An explanation of what the topic includes, for human referance. |

For example, topics could be listed like:

```
"topics": [
  {"name": "Vectors", "color": "blue3", "description": "Vector algebra in 3D."},
  {"name": "Center of mass", "color": "green3", "description": "Calculating the center of mass for irregular bodies and systems."}
],
```

## Tags

Reference: ([link](https://prairielearn.readthedocs.io/en/latest/course/#tags))

