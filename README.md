# resource-detector

- 项目名称：进程内存和 CPU 使用情况采集器 demo
- 版本：v1.1
- 相对于 v1.0 的改进：
  - 数据采集任务间隔为 1 秒，同时在内存里维护一份目标进程列表，数据采集改用进程的方式
  - sqlite 只持久化需要采集的进程元信息，不持久化具体资源变化数据
  - 新增一个 sse 接口，对外提供进程资源变化数据
- 安装和启动：
  ```
  pip install -r requirements.txt
  python run.py
  ```
