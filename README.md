# githook
very simple github webhook server
- 依赖flask
- 配置文件范例
```javascript
{
  "port":9002,
  "address":"localhost",
  "path":"/githook/",
  "log":"githook.log",
  "hooks":{
    "test":{
      "commands":"echo 'helloworld' > test.txt"
    }
  }
}
```
- 如果使用标准的wsgi服务器则忽略port和address
- 然后现在就可以访问 localhost:9002/githook/test 来调用命令行了（只支持post)
