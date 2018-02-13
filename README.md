# Overview

*eiken_listening_tests* is a tool for turning simple text files into 
valid JSON that can be used by 
*[beaunus_clip_splicer](https://github.com/beaunus/ReaScripts/tree/master/Various/beaunus_clip_splicer)*.

An **eiken_listening_test script** looks something like this:

```
Eiken Grade 5 Listening
[Section] 1
#1
  A: I went to Kyoto last month.
  B: Really? I Like Kyoto very much.
  A: Why?
  [Choices]
    1. B: It is in Kansai.
    2. B: It was beautiful.
    3. B: I am from Okinawa.
```

A **beaunus_clip_splicer JSON file** looks something like this:

```
{
  "path": "clips",
  "name": "Eiken Grade 5 Listening",
  "type": "REGION",
  "components": [
    {
      "name": "1",
      "type": "REGION",
      "components": [
        {
          "name": "Track 01 - Question 1",
          "type": "REGION",
          "components": [
            {
              "length": 0.2,
              "track": "PAUSES",
              "name": "PAUSE at beginning of track",
              "type": "MEDIA ITEM"
            },
            {
              "filename": "F/I went to Kyoto last month.",
              "track": "F",
              "name": "F/I went to Kyoto last month.",
              "type": "MEDIA ITEM"
            },
            {
              "length": 0.2,
              "track": "Pauses",
              "name": "Pause after_prompt",
              "type": "MEDIA ITEM"
            },
            {
              "filename": "M/Really? I Like Kyoto very much.",
              "track": "M",
              "name": "M/Really? I Like Kyoto very much.",
              "type": "MEDIA ITEM"
            },
            {
              "length": 0.2,
              "track": "Pauses",
              "name": "Pause after_prompt",
              "type": "MEDIA ITEM"
            },
            {
              "filename": "F/Why?",
              "track": "F",
              "name": "F/Why?",
              "type": "MEDIA ITEM"
            },
            {
              "length": 0.2,
              "track": "Pauses",
              "name": "Pause after_prompt",
              "type": "MEDIA ITEM"
            },
            {
              "filename": "I/1",
              "track": "I",
              "name": "I/1",
              "type": "MEDIA ITEM"
            },
            {
              "length": 0.2,
              "track": "Pauses",
              "name": "Pause after_number",
              "type": "MEDIA ITEM"
            },
            {
              "filename": "M/It is in Kansai.",
              "track": "M",
              "name": "M/It is in Kansai.",
              "type": "MEDIA ITEM"
            },
            {
              "length": 0.2,
              "track": "Pauses",
              "name": "Pause after_choice",
              "type": "MEDIA ITEM"
            },
            {
              "filename": "I/2",
              "track": "I",
              "name": "I/2",
              "type": "MEDIA ITEM"
            },
            {
              "length": 0.2,
              "track": "Pauses",
              "name": "Pause after_number",
              "type": "MEDIA ITEM"
            },
            {
              "filename": "M/It was beautiful.",
              "track": "M",
              "name": "M/It was beautiful.",
              "type": "MEDIA ITEM"
            },
            {
              "length": 0.2,
              "track": "Pauses",
              "name": "Pause after_choice",
              "type": "MEDIA ITEM"
            },
            {
              "filename": "I/3",
              "track": "I",
              "name": "I/3",
              "type": "MEDIA ITEM"
            },
            {
              "length": 0.2,
              "track": "Pauses",
              "name": "Pause after_number",
              "type": "MEDIA ITEM"
            },
            {
              "filename": "M/I am from Okinawa.",
              "track": "M",
              "name": "M/I am from Okinawa.",
              "type": "MEDIA ITEM"
            },
            {
              "length": 0.2,
              "track": "Pauses",
              "name": "Pause after_choice",
              "type": "MEDIA ITEM"
            },
            {
              "length": 0.2,
              "track": "Pauses",
              "name": "Pause after_question",
              "type": "MEDIA ITEM"
            }
          ]
        }
      ]
    }
  ]
}

```

# Patterns

## Voice abbreviations
```
I: Instructions
A: Voice A
B: Voice B
```

## Specific

### Eiken Grade 5 Listening Test
<dl>
  <dt>第一部</dt>
  <dd>Picture - Prompt - 3 Choice</dd>
  <dt>第二部</dt>
  <dd>Conversation - Question - 3 Choice</dd>
  <dt>第三部</dt>
  <dd>Picture - Description - 3 Choice</dd>
</dl>

## Generic

### Picture - Prompt - 3 Choice

#### Student Procedure

1. Look at the picture.
1. Listen to the prompt.
1. Choose the best response out of 3 choices.

#### Script
* Voice genders need to match pictures. 
* Voice ages need to match pictures.

```
 1. I: Number [X]
 2. A: [Prompt]
 3. I: One.
 4. B: [Response 1]
 5. I: Two.
 6. B: [Response 2]
 7. I: Three.
 8. B: [Response 3]
 9. {Pause}
10. {Repeat 2-9}
```

### Conversation - Question - 3 Choice

#### Student Procedure

1. Listen to the conversation.
1. Listen to the question.
1. Choose best answer out of 3 choices.

#### Script
* Voice genders need to match pictures. 
* Voice ages need to match pictures.

```
1. I: Number [X]
2. A: [Sentence]
3. B: [Sentence]
4. I: Question: [Question]
5. {Pause}
6. {Repeat 2-5}
```

### Picture - Description - 3 Choice

#### Student Procedure

1. Look at the picture.
1. Listen to a series of descriptions.
1. Choose best description out of 3 choices.

#### Script
* Voice genders and ages are irrelevant. 
* Genders alternate.

```
1. I: Number [X]
2. I: One.
3. A: [Description 1]
4. I: Two.
5. A: [Description 2]
6. I: Three.
7. A: [Description 3]
8. {Pause}
9. {Repeat 2-8}
```

# File Format

See [example.txt](example.txt) for an example.