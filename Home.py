import streamlit as st

st.set_page_config(
    page_title="Home",
    layout= "wide",
    page_icon="🏠",
)
st.title("🏠 Home")
st.sidebar.success("🏠 Home")

st.write("""
 # ❓Solana NFT Marketplace's #
 # Methodology #
 In this dashboard, I used python to display charts.
 The data used was obtained from flipsidecrypto and queries link are in pages.
 All the codes of this web app can be seen in this link (Github). 
 
 https://github.com/abolfazl7710/Solana-NFT-Marketplace
"""
)
st.write("""
 # 📝 Introduction #

 # Conceptualizing NFT marketplace #
 It is a platform that makes it simple to store and sell NFTs. These tokens are generally available for purchase or auction at a set price. To use an NFT marketplace, you will need a crypto wallet to store and trade your best NFT tokens.Users have to create an account, upload digital artwork, and sell their work on the marketplace. In general, specialized marketplaces are more popular than conventional ones because they include everything a client would require—specialized marketplaces expertise in promoting online artworks and concentrating on specific target audiences. 
 # NFT Marketplace Functionality #
 Before we understand how to build an NFT marketplace, it is essential to know how an NFT marketplace functions from a client's perspective. In fact, all NFT platforms follow the same procedure. For instance, NFTically is a Non-Fungible Tokens exchange platform. You may open your store on NFTically in a matter of minutes. NFTically provides options for minting, selling, and buying.
 Users must first log in by creating an account on the platform. After creating their account, they can download a digital wallet to store their NFTs.
 The users can list their assets by uploading goods to exhibit their effort. Users can also specify which payment tokens they want to receive and set fees if the platform allows it.

 The next step is to put the products for sale on the market. Users have the option of bidding on a fixed price or an auction. When a user sells an item, a transaction is produced in the user's wallet to start a private transaction smart contract.
 The platform will need to conciliate the data before adding the NFT to the list.
 The NFT marketplace deploys smart contracts, a type of transaction protocol. These protocols control the connections between the supplier and the buyer.Furthermore, these smart contracts include NFT-specific identifying data. As a result, buying and selling tokens becomes more accessible and convenient.
 """
 )

st.write("")
st.write("")
st.write("")
st.write("📓 Contact data")
c1, c2 = st.columns(2)
with c1:
    st.info('**Twitter: [@daryoshali](https://twitter.com/daryoshali)**')
with c2:
    st.info('**Data: [Github](https://github.com/abolfazl7710)**')

st.write("")
st.write("")
st.write("")
st.write("Thanks for MetricsDAO and flipsidecrypto team")
