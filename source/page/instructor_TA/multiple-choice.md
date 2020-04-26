## Multiple Choice

Reference: ([link](https://prairielearn.readthedocs.io/en/latest/elements/#pl-multiple-choice-element))

The multiplice choice only requires you to modify:

| Folder/File Name                               | Usage                                                        |
| ---------------------------------------------- | ------------------------------------------------------------ |
| **if this is a standalone problem:** info.json | The information of the question such as title, topic, tags, and uuid. |
| question.html                                  | The main body of the question                                |

A `pl-multiple-choice` element selects **one** correct answer and zero or more
incorrect answers and displays them in a random order as radio buttons.

#### An example of the `question.html`

```html
<pl-question-panel>
	<p> 
	This is the problem statement.
	</p>
</pl-question-panel>

<pl-question-panel><hr></pl-question-panel>
<pl-question-panel>
	<p>
	    (a) 1+1=?
	</p>
</pl-question-panel>

<div class="card my-2">
    <div class="card-body">
        <pl-question-panel>
            <p> 
                The answer is:
            </p>
        </pl-question-panel>

        <pl-multiple-choice answers-name="answer_a" weight="2">
        	<pl-answer correct="false"> 1 </pl-answer>
		    	<pl-answer correct="false"> 3 </pl-answer> 
		    	<pl-answer correct="true"> 2 </pl-answer> 
        </pl-multiple-choice>

    </div>
</div>
```

The problem will be:

![pl-multiple-choice](./elements/pl-multiple-choice-problem.png)

When you clicked the correct answer:

![pl-multiple-choice](./elements/pl-multiple-choice-answer.png)

#### Customizations

| Attribute        | Type    | Default | Description                                                  |
| ---------------- | ------- | ------- | ------------------------------------------------------------ |
| `answers-name`   | string  | —       | Variable name to store data in.                              |
| `weight`         | integer | 1       | Weight to use when computing a weighted average score over elements. |
| `inline`         | boolean | false   | List answer choices on a single line instead of as separate paragraphs. |
| `number-answers` | integer | special | The total number of answer choices to display. Defaults to displaying one correct answer and all incorrect answers. |
| `fixed-order`    | boolean | false   | Disable the randomization of answer order.                   |

Inside the `pl-multiple-choice` element, each choice must be specified with
a `pl-answer` that has attributes:

| Attribute | Type    | Default | Description                               |
| --------- | ------- | ------- | ----------------------------------------- |
| `correct` | boolean | false   | Is this a correct answer to the question? |