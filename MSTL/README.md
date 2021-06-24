# MSTL (Monyhar Super Text Language)

## What is MSTL?

- It's a new front-end language which build for Monyhar Browser
- It breaks west country programming society rules

## MSTL 1.0

- 为了和西方内核兼容，并且逐步替换西方 HTML 语言，我们需要将 MSTL 以西方 HTML 注释的形式嵌入网页中，就像这样：

```MSTL
<!--monyhar
    //your MSTL codes here.
-->
```

- 这是在西方 HTML 中的实现：

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!--monyhar
        //your MSTL codes here.
    -->
</body>
</html>
```

- 这是纯净的 MSTL 语言的实现，文件的后缀名为 `*.mstl`。现阶段需要做到兼容西方内核，所以目前不建议使用。

```MSTL
<Monyhar>
<!--monyhar
    //your MSTL codes here.
-->
```

- MSTL 1.0 版本只规定了如何在西方 HTML 页面中嵌入 MSTL，或者使用纯净的 MSTL 页面。
- MSTL 1.0 版本只要求自主研发内核解析正则表达式为 `<!--harmony[\\s\\S]*-->` 的 MSTL 代码段，不要求解析内部的语法树。即只需要原样输出 MSTL 代码段里的内容即可。
- 目前完整实现 MSTL 1.0 的语言
    - C#