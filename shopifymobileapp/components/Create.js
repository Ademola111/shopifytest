import React from 'react'
import {Text, View, StyleSheet} from 'react-native'

function Create() {
  return (
    <View style={innerHeader.container}>
            <Text style={{margin:10}}>
                Create Inventory
            </Text>
            <Text style={{margin:10}}>
                Add Products
            </Text>
    </View>
  )
}

// stylesheet for the inner header
const innerHeader = StyleSheet.create({
  container: {
  //   flex: 0,
    alignItems: 'center',
    display:'flex',
    justifyContent: 'space-between',
    flexDirection:'row',
    padding:15,
  },
})


export default Create