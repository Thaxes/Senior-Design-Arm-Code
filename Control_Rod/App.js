import React from 'react';
import { StyleSheet, Button, View, SafeAreaView, Text, Alert, TouchableOpacity,} from 'react-native';

const Separator = () => (
  <View style={styles.separator} />
);






const App = () => (
  <SafeAreaView style={styles.container}>
    <View>
      <Text style={styles.title}>
        This is the up button that will be sending a response to the backend.
      </Text>
      <AppButton
        title="🔼"
        
        onPress={() => Alert.alert('Up Button')}
        // onPress={fetch(localhost:5000/up)} Jake's code
      />
    </View>
    <Separator />
    <View>
      <Text style={styles.title}>
        This is the down button that will be sending a response to the backend.
      </Text>
      <AppButton
        title="🔽"
        color="#f194ff"
        onPress={() => Alert.alert('Down Button')}
      />
    </View>
    <Separator />
    
    <Separator />
    <View>
      <Text style={styles.title}>
        
      </Text>
      <View style={styles.fixToText}>
        
        <StopButton
          title="STOP"
          onPress={() => Alert.alert('Re-Rassor Rover will now STOP. Please wait.')}
          
          

        />
      </View>
    </View>
  </SafeAreaView>
);


//

//Custom button
const AppButton = ({ onPress, title }) => (
  <TouchableOpacity onPress={onPress} style={styles.appButtonContainer}>
    <Text style={styles.appButtonText}>{title}</Text>
  </TouchableOpacity>
);

//Custom button
const StopButton = ({ onPress, title }) => (
  <TouchableOpacity onPress={onPress} style={styles.stopButtonContainer}>
    <Text style={styles.appButtonText}>{title}</Text>
  </TouchableOpacity>
);

const styles = StyleSheet.create({ //this aligns the margins
  container: {
    flex: 1,
    justifyContent: 'center',
    marginHorizontal: 20,
    
    
  },
  title: { //this aligns the text that is visible
    textAlign: 'center',
    marginVertical: 20,
    
  },
  fixToText: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  separator: {
    marginVertical: 8,
    borderBottomColor: '#737373',
    borderBottomWidth: StyleSheet.hairlineWidth,
  },
 Button: {
  
 },appButtonContainer: {
    elevation: 8,
    backgroundColor: "#48a5bd",
    borderRadius: 10,
    paddingVertical: 10,
    paddingHorizontal: 12,
  },
  appButtonText: {
    fontSize: 18,
    color: "#fff",
    fontWeight: "bold",
    alignSelf: "center",
    textTransform: "uppercase"
  },
  stopButtonContainer: {
    elevation: 8,
    backgroundColor: "#B30202",
    borderRadius: 10,
    paddingVertical: 10,
    paddingHorizontal: 12,
    justifyContent: 'center',
    alignItems: 'center',
    alignSelf: 'center',
    position: 'relative',
    flex: 1
  },
});
  


export default App;