import { FlatList, StyleSheet, Text, View } from 'react-native';
import Home from './components/Home';
import Inventory from './components/Inventory';
import Create from './components/Create';
import Bags from './components/Bags';
import Shoes from './components/Shoes';
import Caps from './components/Caps';
import Belts from './components/Belts';
import Glasses from './components/Glasses';

import Contants from 'expo-constants';


import { NavigationContainer } from '@react-navigation/native';
// import { createStackNavigator } from '@react-navigation/stack';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator()

function App() {
  return (
    <View style={styles.container}>
      <Stack.Navigator>
        <Stack.Screen name= "Kinsha Stores" component = {Home}/>
        <Stack.Screen name= "Inventory" component = {Inventory}/>
        <Stack.Screen name= "Create" component = {Create}/>
        <Stack.Screen name= "Bags" component = {Bags}/>
        <Stack.Screen name= "Shoes" component = {Shoes}/>
        <Stack.Screen name= "Caps" component = {Caps}/>
        <Stack.Screen name= "Belts" component = {Belts}/>
        <Stack.Screen name= "Glasses" component = {Glasses}/>

        


      </Stack.Navigator>
      
    </View>
  );
}

export default() => {
  return (
    <NavigationContainer>
      <App/>
    </NavigationContainer>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#edff44',
    // alignItems: 'center',
    // marginTop:20,
    marginTop:Contants.statusBarHeight
  },
});
