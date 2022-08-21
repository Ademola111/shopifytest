
import React, {useState, useEffect} from 'react'
import { FlatList, View, Text, StyleSheet, Image} from 'react-native'
import {Card} from 'react-native-paper';

function Bags(props) {

    const [data, setData] = useState([])

    useEffect(() =>{
        fetch("http://127.0.0.1:5000/product/bags/v1/", {
            method:'GET'
        })
        .then(resp => resp.json())
        .then(results => {
            setData(results)
        })
        .catch(function(error){
            console.log(error)
        })

    }, [])

    const renderData = (item) =>{
        return (
            <Card style={style.bag}>
                <Text>{item.name}</Text>
                <Text>{item.price}</Text>
            </Card>
        )
    }

  return (
    <View>
    <FlatList
    data = {data}
    renderItem = {({item}) => {
        // return console.log(item)
        return renderData(item)
    }}
    keyExtractor = {item => `${item.id}`}
    
    />
    
    </View>
  )
}

const style = StyleSheet.create({
    bag:{
        bakgroundColor:'#edff44',
        fontSize:15,
        marginTop:15,
        margin:15,
        padding:15,
        alignItem:'center'
    }
})

export default Bags