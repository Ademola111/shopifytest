

import React, {useState, useEffect} from 'react';
import {Text, View, FlatList, StyleSheet} from 'react-native';
import {Card} from 'react-native-paper';


function Inventory(props) {
  return (
    <View >
        <View style={cardstyle.container}>
            <Card style={eachcardstyle.container} onPress = {() => props.navigation.navigate('Bags')}>
                <Text style={eachinvtyle.container}>Bags</Text>
            </Card>

            <Card style={eachcardstyle.container} onPress = {() => props.navigation.navigate('Shoes')}>
                <Text style={eachinvtyle.container}>Shoes</Text>
            </Card>
        </View>
    
        <View style={cardstyle.container}>
            <Card style={eachcardstyle.container} onPress = {() => props.navigation.navigate('Caps')}>
                <Text style={eachinvtyle.container}>Caps</Text>
            </Card>

            <Card style={eachcardstyle.container} onPress = {() => props.navigation.navigate('Glasses')}>
                <Text style={eachinvtyle.container}>Glasses</Text>
            </Card>
        </View>
        <View style={cardstyle.container}>
            <Card style={eachcardstyle.container} onPress = {() => props.navigation.navigate('Belts')}>
                <Text style={eachinvtyle.container}>Belts</Text>
            </Card>
            <Card style={eachcardstyle.container}>
                <Text style={eachinvtyle.container}>Exit</Text>
            </Card>
        </View>
    </View>
  )
}

const cardstyle = StyleSheet.create({
    container:{
        display:'flex',
        flexDirection:'row',
        justifyContent:'space-between',
        margin:20,
    }
})

const eachcardstyle = StyleSheet.create({
    container:{
        width:110,
        height:110,
        margin:20,
        padding:20,
        fontSize:50,
        alignItems:'center',
        backgroundColor:'orange'
    }
})

const eachinvtyle = StyleSheet.create({
    container:{
        padding:5,
        fontSize:16,
        alignItems:'center',
        marginTop:15,
    }
})

export default Inventory