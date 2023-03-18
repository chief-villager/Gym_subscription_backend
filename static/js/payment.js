

// let userpan_id = "{{new_userplan.id}}"

// function payWithPaystack() {
//   var handler = PaystackPop.setup({
//     key: 'pk_test_e7a885d24ba1ecea0f5f28721756445744a28230', // Replace with your public key
//     email: "{{new_userplan.user.email}}",
//     amount: "{{select_plan.new_price}}", // the amount value is multiplied by 100 to convert to the lowest currency unit
//     currency: 'NGN', // Use GHS for Ghana Cedis or USD for US Dollars
//     ref: "{{new_userplan.new_price}}", // Replace with a reference you generated
//     callback: function(response) {
//       //this happens after the payment is completed successfully
//       var reference = response.reference;
//       alert('Payment complete! Reference: ' + reference);
//       // Make an AJAX call to your server with the reference to verify the transaction
//       $.ajax({
//         url:"http://127.0.0.1:8000/Gym/confirm_payment" + userpan_id,
//         type:"POST"

//       })
//     },
//     onClose: function() {
//       alert('Transaction was not completed, window closed.');
//     },
//   });
//   handler.openIframe();
// }
