实施过程记录

> 总体思想：以hyperledger fabric为方案核心，采用可搜索加密（searchable encryption, SE)和基于属性的访问控制(attribute based access control, ABAC)完成方案实施。

###### 一、hyperledger fabric

**思路：**借助docker容器模拟多机环境，go语言实现智能合约，访问控制和搜索加密的智能合约，上链运行。同时借助fabric的python SDK完成调用智能合约。

**已完成：** 容器构建，容器之间网络连通。

**未完成： ** 加密部分的改进工作。

###### 二、searchable encryption

**思路：**利用charm加密库。智能合约模块有三个方法需要完成：1）init()，实例化智能合约时调用的方法；2）invoke(ciphertext, param)，存储加密数据；3）query()，查询存储的加密关键字。

**已完成：** 智能合约查询和写入已完成。

**未完成：** 加密和python调用代码待完善。

###### 三、attribute based access control

**思路：**在go语言下的casbin库，实现基于属性的访问控制。智能合约有两个接口信息需要完成：1）init()，在instantiated阶段调用的方案，完成合约的实例化；2）invoke(args [])，调用访问控制模块时，判断访问主体是否符合访问控制的条件要求，返回true或false。

**已完成：** 访问控制的智能合约已完成。合约的python调用也已完成。

**未完成：** 暂无。