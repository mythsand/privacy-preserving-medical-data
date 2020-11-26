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
	"strconv"
	"encoding/json"

	"github.com/hyperledger/fabric/core/chaincode/shim"
	pb "github.com/hyperledger/fabric/protos/peer"
)

// S1Chaincode example simple Chaincode implementation
type S1Chaincode struct {
}

func (t *S1Chaincode) Init(stub shim.ChaincodeStubInterface) pb.Response {
	fmt.Println("ex02 Init")
	_, args := stub.GetFunctionAndParameters()
	var A, B string    // Entities
	var Aval, Bval int // Asset holdings
	var err error

	if len(args) != 4 {
		return shim.Error("Incorrect argument numbers. Expecting 4")
	}

	// Initialize the chaincode
	A = args[0]
	Aval, err = strconv.Atoi(args[1])
	if err != nil {
		return shim.Error("Expecting integer value for asset holding")
	}
	B = args[2]
	Bval, err = strconv.Atoi(args[3])
	if err != nil {
		return shim.Error("Expecting integer value for asset holding")
	}
	fmt.Printf("Aval = %d, Bval = %d\n", Aval, Bval)

	// Write the state to the ledger
	err = stub.PutState(A, []byte(strconv.Itoa(Aval)))
	if err != nil {
		return shim.Error(err.Error())
	}

	err = stub.PutState(B, []byte(strconv.Itoa(Bval)))
	if err != nil {
		return shim.Error(err.Error())
	}

	return shim.Success(nil)
}

func (t *S1Chaincode) Invoke(stub shim.ChaincodeStubInterface) pb.Response {
	fmt.Println("ex02 Invoke")
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

func (t *S1Chaincode) query(stub shim.ChaincodeStubInterface, args []string) pb.Response {
    startKey := "startkey"
    endKey := "endkey"

    if len(args) != 2 {
		return shim.Error("Incorrect number of arguments. Expecting 2")
	}

	type res struct{
		Key string `json:"key"`
		Valu string `json:"valu"`
	}

	var resArr []res

	startKey = args[0]
	endKey = args[1]
    // 根据范围查询, 得到StateQueryIteratorInterface迭代器接口
    keysIter, err := stub.GetStateByRange(startKey, endKey)
    // 最后关闭迭代器接口
    defer keysIter.Close()
    var keys []string
    for keysIter.HasNext() {	// 如果有下一个节点
        // 得到下一个键值对
        response, iterErr := keysIter.Next()
        if iterErr != nil {
            return shim.Error(fmt.Sprintf("find an error %s", iterErr))
        }
        keys = append(keys, response.Key)	// 存储键值到数组中
        valu, err := stub.GetState(response.Key)
        if err != nil {
			jsonResp := "{\"Error\":\"Failed to get state for " + response.Key + "\"}"
			return shim.Error(jsonResp)
		}

		res_temp := res{
			Key: response.Key,
			Valu: string(valu),
		}

		resArr = append(resArr, res_temp)
	}
    
    // 遍历keys数组
    // for key, value := range keys {
    //     fmt.Printf("key %d contains %s\n", key, value)
    // }
    // 编码keys数组成json格式
    jsonKeys, err := json.Marshal(resArr)
    if err != nil {
        return shim.Error(fmt.Sprintf("data Marshal json error: %s", err))
    }
    
    // 将编码之后的json字符串传递给客户端
    jsonres := string(jsonKeys)
    jsonresby := []byte(jsonres)
    return shim.Success(jsonresby)
};

// Transaction makes payment of X units from A to B
func (t *S1Chaincode) invoke(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	var A string    // Entities
	var Aval string // Asset holdings
	// var X int          // Transaction value
	// var err error

	if len(args) != 2 {
		return shim.Error("Incorrect number of arguments. Expecting 2")
	}

	A = args[0]
	Aval = args[1]

	// Get the state from the ledger
	// TODO: will be nice to have a GetAllState call to ledger
	_, err := stub.GetState(A)
	// if err != nil {
	// 	return shim.Error("Failed to get state")
	// }
	// if Avalbytes == nil {
	// 	return shim.Error("Entity not found")
	// }
	// Aval, _ = strconv.Atoi(string(Avalbytes))

	// Bvalbytes, err := stub.GetState(B)
	// if err != nil {
	// 	return shim.Error("Failed to get state")
	// }
	// if Bvalbytes == nil {
	// 	return shim.Error("Entity not found")
	// }
	// Bval, _ = strconv.Atoi(string(Bvalbytes))

	// Perform the execution
	// X, err = strconv.Atoi(args[2])
	// if err != nil {
		// return shim.Error("Invalid transaction amount, expecting a integer value")
	// }
	// Aval = Aval - X
	// Bval = Bval + X
	// fmt.Printf("Aval = %d, Bval = %d\n", Aval, Bval)

	// Write the state back to the ledger
	err = stub.PutState(A, []byte(Aval))
	if err != nil {
		return shim.Error(err.Error())
	}

	// err = stub.PutState(B, []byte(strconv.Itoa(Bval)))
	// if err != nil {
	// 	return shim.Error(err.Error())
	// }

	payloadAsBytes := []byte(Aval)
	return shim.Success(payloadAsBytes)
}

// Deletes an entity from state
func (t *S1Chaincode) delete(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	if len(args) != 1 {
		return shim.Error("Incorrect number of arguments. Expecting 1")
	}

	A := args[0]

	// Delete the key from the state in ledger
	err := stub.DelState(A)
	if err != nil {
		return shim.Error("Failed to delete state")
	}

	return shim.Success(nil)
}

// query callback representing the query of a chaincode
func (t *S1Chaincode) query1(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	var A string // Entities
	var err error

	if len(args) != 1 {
		return shim.Error("Incorrect number of arguments. Expecting name of the person to query")
	}

	A = args[0]

	// Get the state from the ledger
	Avalbytes, err := stub.GetState(A)
	if err != nil {
		jsonResp := "{\"Error\":\"Failed to get state for " + A + "\"}"
		return shim.Error(jsonResp)
	}

	if Avalbytes == nil {
		jsonResp := "{\"Error\":\"Nil amount for " + A + "\"}"
		return shim.Error(jsonResp)
	}

	jsonResp := "{\"Name\":\"" + A + "\",\"Amount\":\"" + string(Avalbytes) + "\"}"
	fmt.Printf("Query Response:%s\n", jsonResp)

	return shim.Success(Avalbytes)
}

func main() {
	err := shim.Start(new(S1Chaincode))
	if err != nil {
		fmt.Printf("Error starting Simple chaincode: %s", err)
	}
}
