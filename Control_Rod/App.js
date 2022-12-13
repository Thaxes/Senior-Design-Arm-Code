import React from "react";
import {
    StyleSheet,
    Button,
    View,
    SafeAreaView,
    Text,
    Alert,
    TouchableOpacity,
} from "react-native";

const Separator = () => <View style={styles.separator} />;

const fetcher = async (endpoint) => {
    console.log(endpoint); // this variable value should be the endpoint route that is attempted to be called without the first forward slash
    // an example is 'shoulder/up'
    try {
        let response = await fetch(`http://10.0.2.2:5000/${endpoint}`, {
            method: "GET", // using a get request instead of a post to make sure the ROS is getting the message by the backend sending a message back to me
            headers: {
                Accept: "application/json",
            },
        });
        if (!response.ok) {
            // if the response sent back is not correct or there is no response an error is thrown with the status of the response
            throw new Error(`Error! status: ${response.status}`);
        }
        const result = await response.json();

        console.log("result is: ", JSON.stringify(result, null, 4));
    } catch (err) {
        console.log(err);
    }
};

const App = () => (
    <SafeAreaView style={styles.container}>
        <View>
            <Text style={styles.title}>
                This is the up button that will be sending a response to the
                backend.
            </Text>
            <AppButton title='🔼' onPress={() => fetcher("shoulder/up")} />
        </View>
        <Separator />
        <View>
            <Text style={styles.title}>
                This is the down button that will be sending a response to the
                backend.
            </Text>
            <AppButton
                title='🔽'
                color='#f194ff'
                onPress={() => fetcher("shoulder/down")}
            />
        </View>
        <Separator />

        <Separator />
        <View>
            <Text style={styles.title}></Text>
            <View style={styles.fixToText}>
                <StopButton
                    title='STOP'
                    onPress={() => fetcher("shoulder/stop")}
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

const styles = StyleSheet.create({
    //this aligns the margins
    container: {
        flex: 1,
        justifyContent: "center",
        marginHorizontal: 20,
    },
    title: {
        //this aligns the text that is visible
        textAlign: "center",
        marginVertical: 20,
    },
    fixToText: {
        flexDirection: "row",
        justifyContent: "space-between",
    },
    separator: {
        marginVertical: 8,
        borderBottomColor: "#737373",
        borderBottomWidth: StyleSheet.hairlineWidth,
    },
    Button: {},
    appButtonContainer: {
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
        textTransform: "uppercase",
    },
    stopButtonContainer: {
        elevation: 8,
        backgroundColor: "#B30202",
        borderRadius: 10,
        paddingVertical: 10,
        paddingHorizontal: 12,
        justifyContent: "center",
        alignItems: "center",
        alignSelf: "center",
        position: "relative",
        flex: 1,
    },
});

export default App;
