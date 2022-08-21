


import React from 'react';
import {Text, View, StyleSheet, FlatList} from 'react-native';
import {FAB} from 'react-native-paper';


function Home(props) {
  return (
    <View style={{alignItems:'center', flex:1}} > 
        <View style={logo.cnti}>
        <Text>Welcome to Kinsha Stores</Text>
        <Text>Click inventory to begin</Text>    
        <Text style={logo.container} onPress = {() => props.navigation.navigate('Inventory')} icon='product'>Inventory</Text>
        </View>
        <FAB
        style={logo.fab}
        small = {false}
        icon ='plus'
        theme={{colors:{accent:'green'}}}
        onPress = {() => props.navigation.navigate('Create')}
        />
    </View>
    
    
  );
}


// stylesheet for the logo
const logo = StyleSheet.create({
    container:{
        width:130, 
        height:50, 
        backgroundColor:'orange', 
        padding:10, 
        color:'white',
        fontSize:25,
        margin:10,
        alignItems:'center'
    },

// fab style
    fab:{
        position:"absolute",
        margin:16,
        right:0,
        bottom:0
    
    },

    cnti:{
        position:"absolute",
        marginTop:250,
        alignItems:'center'
    }
})



// stylesheet for the main header
// const mainHeader = StyleSheet.create({
//     container:{
//         marginTop:15, 
        // display:'flex', 
        // flexDirection:'row', justifyContent:'space-between'
//     }
// })


export default Home