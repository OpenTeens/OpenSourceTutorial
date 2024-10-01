# 写新文章 / Write new tutorial
向 `tutorial/src` 文件夹中提交 `comp-md` 格式的文件，后缀名为 `.md`。

其中，`src`文件夹分三级，比如：`book1/section1/welcome.md`，其中第一级为书名/系列名，第二级为章节名，第三级为文章名。章节名和文章名均会显示在编译之后的教程页面中。

# Comp-md 格式 / The comp-md standard
- 主体部分同 markdown 一样
- 可以使用 `-----COMP_NAME-----` （前后均有五个`-`） 来启用组件
- 组件各部分之间有一个空行
- 组件以 `-----COMP_NAME-----` 标志结束

## 组件 / Components
### choose
调用方法：使用 `-----choose-----` 以调用该组件。

部分一：问题（纯文本，不可使用markdown语法）

部分二：选项（格式形如`- [ ] answer1`，注意空格。方括号内若有`*`则表示该选项为答案。组件会自动判定单选/多选题。）

示例：
```markdown
调用 `choose` 组件的示例：

-----choose-----
What is the **answer** to the universe?

- [ ] 41
- [*] 42
- [ ] 43
- [ ] 44
-----choose-----
```

