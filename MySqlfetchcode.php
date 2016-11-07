<?php

$servername = "xxx";
$username = "xxxx";
$password = "xxxx";
$dbname = "myDB";

// Create connection 
$conn = new mysqli($servername, $username, $password, $dbname);

//Check connection
if ($conn->connect_error) {
	die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT id, xxxxx, xxxxxx FROM Table_name";
$result = $conn->query($sql);

if ($result->num_rows > 0 ) {
	//output data of each row
	while($row = $result->fetch_assoc()) {
		echo "id: " .$row["id"]. "- xxxx: " .$row["xxxxx"]. "<br>";
	}
} else {
	echo "0 results";
}
$conn->close();

?>
