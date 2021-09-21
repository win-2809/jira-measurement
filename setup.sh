mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
<<<<<<< HEAD
" > ~/.streamlit/config.toml
=======
" > ~/.streamlit/config.toml
>>>>>>> cebafefb170843d3daca17976b6420cb65303f54
