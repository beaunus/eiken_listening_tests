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

## Example
```
Eiken Grade 5 Listening - 第１回 // The first line in the project title.
[Section] 大問１ // [Section] lines will begin a new region.
#1 [M,F] // Note the # symbol. The M and F refer to the genders.
  A: I went to Kyoto last month. // Parenthetical notes are optional.
  B: Really? I Like Kyoto very much.
  A: Why?
  [Choices] // This symbol indicates that the Instruction voice should read "One", "Two", etc. before the character voice reads the choice.
    1. B: It is in Kansai. // Note the character name.
    2. B: It was beautiful.
    3. B: I am from Okinawa.
#2
  A: I want to go shopping. // Characters without parenthetical parameters have the gender chosen at random.
  B: What are you going to buy? // The opposing character will have the opposite gender, by default.
  A: Just some bread. Would you like to come with me?
  [Choices]
    1. B: He went this morning.
    2. B: Sure. Let me get my jacket.
    3. B: I have no bread.
[Section]: 大問2
#3 [F,M]
  A: How was Hokkaido?
  B: It was great.
  A: Didn't you go there last winter, too?
  B: No. We went to Hiroshima and Osaka.
  [Question] Where did he go this year? // This tag indicates that the Instruction voice should read "Question", followed by the question itself.
  [Choices]
    1. Osaka.
    2. Hiroshima.
    3. Hokkaido.
    4. He didn't go anywhere.
#4 [F,M]
  A: I smell something sweet?
  B: Yes. I have some cupcakes. Would you like one?
  A: Just a small one. I ate too much cereal for breakfast.
  B: Okay.
  [Question] What did she have for breakfast?
  [Choices]
    1. Sweet potato.
    2. Cupcakes.
    3. Peas.
    4. Cereal.
[Section]: 大問3
#5 [M]
  A: It is very cold this winter. I can’t wait for spring to start. But my favorite season is summer. Every summer I go to swim in the sea.
  [Question] What is his favorite season?
  [Choices - Not spoken] // This tag indicates that the choices are not spoken. This is so answer choices can be included in the script, even if they are not spoken.
    1. Spring
    2. Summer
    3. Fall
    4. Winter
#6
  A: Jake’s father is a music teacher. Jake started playing the guitar at five years old. His sister Meg plays the piano. They love music.
  [Question] Who plays the piano?
  [Choices - Not spoken]
    1. Jake.
    2. Jake’s father.
    3. Jake’s mother.
    4. Jake’s sister.
```