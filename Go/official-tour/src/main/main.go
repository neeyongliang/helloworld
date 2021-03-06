package main

import (
	"basics"
	"fmt"
	"welcome"
)

import (
	"concurrency"
	"flowcontrol"
	"methods"
	"moretypes"
)

func main() {
	fmt.Println("example001")
	welcome.SayHello()
	fmt.Println("example002")
	welcome.GetTime()
	fmt.Println("example003")
	basics.TestImports()
	fmt.Println("example004")
	basics.TestPackages()
	fmt.Println("example005")
	basics.TestPrintPi()
	fmt.Println("example006")
	basics.TestAdd(42, 13)
	fmt.Println("example007")
	basics.TestAdd2(53, 2)
	fmt.Println("example008")
	basics.TestSwap("hello", "world")
	fmt.Println("example009")
	basics.TestSplit(17)
	fmt.Println("example010")
	basics.TestVariables()
	fmt.Println("example011")
	basics.TestVariables2()
	fmt.Println("example012")
	basics.TestShortVar()
	fmt.Println("example013")
	basics.TestBasicTypes()
	fmt.Println("example014")
	basics.TestZero()
	fmt.Println("example015")
	basics.TestTypeConver()
	fmt.Println("example016")
	basics.TestTypeInfer()
	fmt.Println("example017")
	basics.TestConstant()
	fmt.Println("example018")
	basics.TestNumericConst()
	fmt.Println("example019")
	flowcontrol.TestFor()
	fmt.Println("example020")
	flowcontrol.TestFor2()
	fmt.Println("example021")
	flowcontrol.TestWhile()
	fmt.Println("example022")
	flowcontrol.TestIf()
	fmt.Println("example023")
	flowcontrol.TestIfStatement()
	fmt.Println("example024")
	flowcontrol.TestIfAndElse()
	fmt.Println("example025")
	flowcontrol.TestWhile()
	fmt.Println("example026")
	flowcontrol.ExerciseFlowControl()
	fmt.Println("example027")
	flowcontrol.TestSwitch()
	fmt.Println("example028")
	flowcontrol.TestSwitchOrder()
	fmt.Println("example029")
	flowcontrol.TestSwitchNoCondition()
	fmt.Println("example030")
	flowcontrol.TestDefer()
	fmt.Println("example031")
	flowcontrol.TestDeferMulti()
	fmt.Println("example032")
	moretypes.TestPointers()
	fmt.Println("example033")
	moretypes.TestStruct()
	fmt.Println("example034")
	moretypes.TestStructFields()
	fmt.Println("example035")
	moretypes.TestStructPointers()
	fmt.Println("example036")
	moretypes.TestArray()
	fmt.Println("example037")
	moretypes.TestArraySlice()
	fmt.Println("example038")
	moretypes.TestSlicesPointers()
	fmt.Println("example039")
	moretypes.TestSliceLiterals()
	fmt.Println("example040")
	moretypes.TestSliceBounds()
	fmt.Println("example041")
	moretypes.TestPrintSlice()
	fmt.Println("example042")
	moretypes.TestNilSlices()
	fmt.Println("example043")
	moretypes.TestMakingSlices()
	fmt.Println("example044")
	moretypes.TestSlicesOfSlice()
	fmt.Println("example045")
	moretypes.TestSliceAppend()
	fmt.Println("example046")
	moretypes.TestRange()
	fmt.Println("example047")
	moretypes.TestRangeContinue()
	fmt.Println("example048")
	moretypes.ExercieseMyPic()
	fmt.Println("example049")
	moretypes.TestMaps()
	fmt.Println("example050")
	moretypes.TestMapLiterals()
	fmt.Println("example051")
	moretypes.TestMapsLiteralsContinue()
	fmt.Println("example052")
	moretypes.TestMutatingMaps()
	fmt.Println("example053")
	moretypes.ExerciseMaps()
	fmt.Println("example054")
	moretypes.TestFunctionValues()
	fmt.Println("example055")
	moretypes.TestFunctionClosures()
	fmt.Println("example056")
	moretypes.ExerciseFabonacci()
	fmt.Println("example057")
	methods.TestMethods()
	fmt.Println("example058")
	methods.TestMethods2()
	fmt.Println("example059")
	methods.TestMethods3()
	fmt.Println("example060")
	methods.TestMethodsPointers()
	fmt.Println("example061")
	methods.TestMethodsPointersExplained()
	fmt.Println("example062")
	methods.TestIndirection()
	fmt.Println("example063")
	methods.TestIndirectionValues()
	fmt.Println("example064")
	methods.TestWithPointerReceivers()
	fmt.Println("example065")
	methods.TestInterfaces()
	fmt.Println("example066")
	methods.TestInterfacesSatisfiedImplicitly()
	fmt.Println("example067")
	methods.TestInterfacesValues()
	fmt.Println("example068")
	methods.TestInterfaceValueWithNil()
	fmt.Println("example069")
	methods.TestEmptyInterface()
	fmt.Println("example070")
	methods.TestTypeAssertions()
	fmt.Println("example071")
	methods.TestTypeSwitches()
	fmt.Println("example072")
	methods.TestStringer()
	fmt.Println("example073")
	methods.ExerciseStringer()
	fmt.Println("example074")
	methods.TestError()
	fmt.Println("example075")
	methods.ExerciseError()
	fmt.Println("example076")
	methods.TestReader()
	fmt.Println("example077")
	methods.ExerciseReader()
	fmt.Println("example078")
	methods.ExerciseRot13Reader()
	fmt.Println("example079")
	methods.ExerciseImages()
	fmt.Println("example080")
	concurrency.TestGoroutines()
	fmt.Println("example081")
	concurrency.TestChannels()
	fmt.Println("example082")
	concurrency.TestBufferedChannels()
	fmt.Println("example083")
	concurrency.TestRangeAndClose()
	fmt.Println("example084")
	concurrency.TestSelect()
	fmt.Println("example085")
	concurrency.TestDefaultSelection()
	fmt.Println("example086")
	concurrency.ExerciseEqBinaryTree()
	fmt.Println("example087")
	concurrency.TestMutexCounter()
	fmt.Println("example088")
	concurrency.ExerciseWebCrawler()
}
