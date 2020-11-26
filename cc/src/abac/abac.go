/*
Copyright IBM Corp. 2016 All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

		 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package main

import (
	"fmt"

	"github.com/casbin/casbin/v2"
	"github.com/casbin/casbin/v2/model"

	"github.com/hyperledger/fabric/core/chaincode/shim"
	pb "github.com/hyperledger/fabric/protos/peer"
)

// S2Chaincode example simple Chaincode implementation
type S2Chaincode struct {
}

// Env : env var
type Env struct {
	IP string
	OS string
}

// CheckIp ip
func (env *Env) CheckIp() bool {
	fmt.Println(env.IP, env.OS)
	return true
}

// TCheck os
func (env *Env) TCheck(os string) bool {
	fmt.Println(env.IP, env.OS, os)
	return true
}

//不实现判断逻辑，仅看是否能获取参数
const modelText6 = `
[request_definition]
r = sub, obj, act, env
[policy_definition]
p = sub, obj, act, ip, os
[policy_effect]
e = some(where (p.eft == allow))
[matchers]
m = r.sub == p.sub && r.obj == p.obj && r.act == p.act && r.env.TCheck(p.os)
`

func test() {
	env := &Env{}
	env.IP = "192.168.1.100"
	env.OS = "linux"
	m := model.Model{}
	m.LoadModelFromText(modelText6)
	e, _ := casbin.NewEnforcer(m, true)

	e.AddPolicy("alice", "d1", "read", "1.1.1.1", "Centos")
	e.AddPolicy("alice", "d2", "read", "2.2.2.2", "Mac")

	result, _ := e.Enforce("alice", "data1", "read", env)

	fmt.Println(result)
}

// Init method
func (t *S2Chaincode) Init(stub shim.ChaincodeStubInterface) pb.Response {
	fmt.Println("cc-abac Init")
	_, args := stub.GetFunctionAndParameters()
	var Init string // env var
	// var err error

	if len(args) != 1 {
		return shim.Error("Incorrect argument numbers. Expecting 1")
	}

	// Initialize the chaincode
	Init = args[0]
	// if err != nil {
	// 	return shim.Error("Expecting integer value for asset holding")
	// }

	fmt.Printf("Aval = %d\n", Init)

	// Write the state to the ledger
	// err = stub.PutState("cc-abac", "init.")
	// if err != nil {
	// 	return shim.Error(err.Error())
	// }

	return shim.Success(nil)
}

//Invoke method
func (t *S2Chaincode) Invoke(stub shim.ChaincodeStubInterface) pb.Response {
	fmt.Println("cc-abac Invoke")

	function, args := stub.GetFunctionAndParameters()
	if function == "invoke" {
		// Make payment of X units from A to B
		return t.invoke(stub, args)
	} else if function == "delete" {
		// Deletes an entity from its state
		return t.delete(stub, args)
	} else if function == "query" {
		// the old "Query" is now implemtned in invoke
		return t.query(stub, args)
	}

	return shim.Error("Invalid invoke function name. Expecting \"invoke\" \"delete\" \"query\"")
}

func (t *S2Chaincode) query(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	// startKey := "startkey"
	// endKey := "endkey"

	// if len(args) != 2 {
	// 	return shim.Error("Incorrect number of arguments. Expecting 2")
	// }

	// type res struct {
	// 	Key  string `json:"key"`
	// 	Valu string `json:"valu"`
	// }

	// var resArr []res

	// startKey = args[0]
	// endKey = args[1]
	// // 根据范围查询, 得到StateQueryIteratorInterface迭代器接口
	// keysIter, err := stub.GetStateByRange(startKey, endKey)
	// // 最后关闭迭代器接口
	// defer keysIter.Close()
	// var keys []string
	// for keysIter.HasNext() { // 如果有下一个节点
	// 	// 得到下一个键值对
	// 	response, iterErr := keysIter.Next()
	// 	if iterErr != nil {
	// 		return shim.Error(fmt.Sprintf("find an error %s", iterErr))
	// 	}
	// 	keys = append(keys, response.Key) // 存储键值到数组中
	// 	valu, err := stub.GetState(response.Key)
	// 	if err != nil {
	// 		jsonResp := "{\"Error\":\"Failed to get state for " + response.Key + "\"}"
	// 		return shim.Error(jsonResp)
	// 	}

	// 	res_temp := res{
	// 		Key:  response.Key,
	// 		Valu: string(valu),
	// 	}

	// 	resArr = append(resArr, res_temp)
	// }

	// // 遍历keys数组
	// // for key, value := range keys {
	// //     fmt.Printf("key %d contains %s\n", key, value)
	// // }
	// // 编码keys数组成json格式
	// jsonKeys, err := json.Marshal(resArr)
	// if err != nil {
	// 	return shim.Error(fmt.Sprintf("data Marshal json error: %s", err))
	// }

	// // 将编码之后的json字符串传递给客户端
	// jsonres := string(jsonKeys)
	// jsonresby := []byte(jsonres)
	// return shim.Success(jsonresby)
	return shim.Success(nil)
}

// Transaction makes payment of X units from A to B
func (t *S2Chaincode) invoke(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	// var A string    // Entities
	// var Aval string // Asset holdings
	// var X int          // Transaction value
	// var err error
	var Sub, Obj, Act, Ip, Os string // env var

	if len(args) != 5 {
		return shim.Error("Incorrect number of arguments. Expecting 5")
	}

	Sub = args[0]
	Obj = args[1]
	Act = args[2]
	Ip = args[3]
	Os = args[4]

	env := &Env{}
	env.IP = Ip
	env.OS = Os
	m := model.Model{}
	m.LoadModelFromText(modelText6)
	e, _ := casbin.NewEnforcer(m, true)

	e.AddPolicy("r1", "d1", "read", "1.1.1.1", "Centos")
	e.AddPolicy("r1", "d2", "read", "2.2.2.2", "Mac")

	result, _ := e.Enforce(Sub, Obj, Act, env)
	var res string
	if result == false {
		res = "false"
	} else {
		res = "true"
	}

	payloadAsBytes := []byte(res)
	return shim.Success(payloadAsBytes)
}

// Deletes an entity from state
func (t *S2Chaincode) delete(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	// if len(args) != 1 {
	// 	return shim.Error("Incorrect number of arguments. Expecting 1")
	// }

	// A := args[0]

	// // Delete the key from the state in ledger
	// err := stub.DelState(A)
	// if err != nil {
	// 	return shim.Error("Failed to delete state")
	// }

	return shim.Success(nil)
}

// query callback representing the query of a chaincode
// func (t *S2Chaincode) query1(stub shim.ChaincodeStubInterface, args []string) pb.Response {
// 	var A string // Entities
// 	var err error

// 	if len(args) != 1 {
// 		return shim.Error("Incorrect number of arguments. Expecting name of the person to query")
// 	}

// 	A = args[0]

// 	// Get the state from the ledger
// 	Avalbytes, err := stub.GetState(A)
// 	if err != nil {
// 		jsonResp := "{\"Error\":\"Failed to get state for " + A + "\"}"
// 		return shim.Error(jsonResp)
// 	}

// 	if Avalbytes == nil {
// 		jsonResp := "{\"Error\":\"Nil amount for " + A + "\"}"
// 		return shim.Error(jsonResp)
// 	}

// 	jsonResp := "{\"Name\":\"" + A + "\",\"Amount\":\"" + string(Avalbytes) + "\"}"
// 	fmt.Printf("Query Response:%s\n", jsonResp)

// 	return shim.Success(Avalbytes)
// }

func main() {
	err := shim.Start(new(S2Chaincode))
	if err != nil {
		fmt.Printf("Error starting Simple chaincode: %s", err)
	}
}
